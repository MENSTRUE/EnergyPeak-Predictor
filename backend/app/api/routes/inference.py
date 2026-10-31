from fastapi import APIRouter
from app.schemas.prediction import FeaturePredictionRequest
from app.inference.predictor import model_file, inspect_artifact, load_model, predict_features
from fastapi import HTTPException

router=APIRouter(tags=['research inference'])

@router.get('/models/{series_id}')
def model_details(series_id: str):
    file=model_file(series_id)
    if not file.is_file():
        return {'series_id':series_id,'available':False,'expected_filename':file.name}
    artifact=load_model(str(file))
    model,names=inspect_artifact(artifact)
    return {'series_id':series_id,'available':True,'expected_filename':file.name,
            'supports_predict':bool(model is not None and hasattr(model,'predict')),
            'feature_names':list(map(str,list(names))) if names is not None else None,
            'production_validated':False}

@router.post('/predict/{series_id}')
def predict(series_id: str, request: FeaturePredictionRequest):
    return predict_features(series_id,request.features)
