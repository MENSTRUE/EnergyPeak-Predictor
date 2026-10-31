"""Research inference: explicit validated feature vectors only.

No timestamp-only or live-grid prediction is invented. Loading joblib is unsafe
with untrusted files: only use your own Kaggle-exported artifacts.
"""
from functools import lru_cache
from pathlib import Path
import math
import numpy as np
import joblib
from fastapi import HTTPException
from app.core.config import settings
from app.services.catalog import valid_id

@lru_cache(maxsize=16)
def load_model(path_str: str):
    path = Path(path_str)
    try:
        return joblib.load(path)
    except Exception as exc:
        raise HTTPException(503, detail=f'Model could not be loaded (check scikit-learn version): {type(exc).__name__}')

def model_file(series_id: str) -> Path:
    valid_id(series_id)
    return settings.model_dir / f'{series_id}_champion.joblib'

def model_available(series_id: str) -> bool:
    return model_file(series_id).is_file()

def inspect_artifact(artifact):
    if isinstance(artifact, dict):
        estimator = artifact.get('model') or artifact.get('pipeline') or artifact.get('estimator')
        names = artifact.get('feature_columns')
        if names is None:
            names = artifact.get('feature_names')
        return estimator, names
    return artifact, getattr(artifact, 'feature_names_in_', None)

def predict_features(series_id: str, features: dict[str, float]):
    path = model_file(series_id)
    if not path.is_file():
        raise HTTPException(503, detail='Model file missing. Copy the trusted champion .joblib into models/champion.')
    artifact = load_model(str(path))
    model, names = inspect_artifact(artifact)
    if model is None or not hasattr(model, 'predict'):
        raise HTTPException(422, detail='Unsupported model artifact structure; inspect Kaggle export contract')
    if names is None:
        raise HTTPException(422, detail='Model has no recorded ordered feature names; cannot safely infer feature order')
    names = list(map(str, list(names)))
    if not names or len(set(names)) != len(names):
        raise HTTPException(422, detail='Invalid feature schema')
    missing = sorted(set(names) - set(features))
    extra = sorted(set(features) - set(names))
    if missing or extra:
        raise HTTPException(422, detail={'missing_features':missing,'extra_features':extra,'required_features':names})
    if not all(math.isfinite(float(v)) for v in features.values()):
        raise HTTPException(422, detail='Features must be finite numbers')
    import pandas as pd
    X = pd.DataFrame([[float(features[n]) for n in names]], columns=names)
    try:
        prediction = float(np.asarray(model.predict(X)).reshape(-1)[0])
    except Exception as exc:
        raise HTTPException(422, detail=f'Model inference failed: {type(exc).__name__}: {str(exc)[:240]}')
    if not math.isfinite(prediction):
        raise HTTPException(422, detail='Non-finite model output')
    return {'series_id':series_id,'prediction':prediction,'n_features':len(names),'method':'one_step_ahead_with_explicit_historical_features','production_validated':False,'source':'trusted_local_joblib'}
