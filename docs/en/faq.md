# Faq — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## FAQ

**Is this live forecasting?** No, the displayed forecast explorer is historical held-out evaluation. **Does 14/14 mean 14 models load?** No, it counts files; loading must be tested separately. **Are the three datasets fused?** No, experiments preserve domain and cadence. **Why Peak F1?** A train-P90 event proxy complements MAE; it does not measure grid emergency. **Can I forecast using date only?** No, saved estimators require exact historical features. **Is the source data included?** No, fetch it subject to its original rights and provenance. **Is the software production-ready?** No.

## Troubleshooting

**API offline:** start backend in its venv and verify health. **CORS:** validate `VITE_API_BASE_URL` and backend allowed origins. **404 metrics:** restore CSV/JSON to exact report paths. **503 missing model:** local `models/champion/{series_id}_champion.joblib` absent. **503 `ModuleNotFoundError: _loss`:** artifact serialized under scikit-learn 1.6.1 but backend previously ran 1.9.1; install/test compatible pinned environment rather than suppressing errors. **Mixed model availability:** filesystem presence != successful `joblib.load`. **422 feature mismatch:** inspect exact `feature_columns` then reconstruct lag/rolling features without future observations. **RAM pressure:** load one large RF at a time. **npm audit:** review advisories and test changes, avoid blind `--force`.

## Scope and claim boundaries

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
