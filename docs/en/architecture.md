# Architecture — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Application architecture and API

**Research layer:** Kaggle notebook creates reports and serialized artifacts. **API:** FastAPI serves health, series inventory, saved metrics, paginated forecast samples, audit/manifest reports and conditional model inspection/prediction. **UI:** React + Vite + TypeScript exposes Overview, Forecast Explorer, Model Inference and Research & Audit. Reports are read-only snapshots. `GET /api/v1/health`, `/api/v1/series`, `/api/v1/series/{series_id}/metrics`, `/api/v1/series/{series_id}/forecast`, `/api/v1/reports/model-manifest`, `/api/v1/reports/{name}`, `/api/v1/models/{series_id}`, `POST /api/v1/predict/{series_id}`. Inference requires the trusted local joblib, exact named historical features, and compatible sklearn version.

## Repository structure

`notebooks/` research master; `data/{raw,interim,processed,external}/` ignored local datasets; `models/{baseline,champion}/` local artifacts (not committed); `reports/{audit,evaluation,experiments,forecasts}/` saved results; `assets/plots/` fourteen real forecast PNGs; `assets/screenshots/` four app captures; `backend/app/` FastAPI; `frontend/src/` React; `docs/{en,id}/` paired documentation; `scripts/` helpers; `tests/` checks; `LICENSE` MIT. See `docs/en/repository-map.md` for a fuller map.

## Scope and claim boundaries

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
