# Api Contract — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Application architecture and API

**Research layer:** Kaggle notebook creates reports and serialized artifacts. **API:** FastAPI serves health, series inventory, saved metrics, paginated forecast samples, audit/manifest reports and conditional model inspection/prediction. **UI:** React + Vite + TypeScript exposes Overview, Forecast Explorer, Model Inference and Research & Audit. Reports are read-only snapshots. `GET /api/v1/health`, `/api/v1/series`, `/api/v1/series/{series_id}/metrics`, `/api/v1/series/{series_id}/forecast`, `/api/v1/reports/model-manifest`, `/api/v1/reports/{name}`, `/api/v1/models/{series_id}`, `POST /api/v1/predict/{series_id}`. Inference requires the trusted local joblib, exact named historical features, and compatible sklearn version.

## Backend and frontend testing

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Troubleshooting

**API offline:** start backend in its venv and verify health. **CORS:** validate `VITE_API_BASE_URL` and backend allowed origins. **404 metrics:** restore CSV/JSON to exact report paths. **503 missing model:** local `models/champion/{series_id}_champion.joblib` absent. **503 `ModuleNotFoundError: _loss`:** artifact serialized under scikit-learn 1.6.1 but backend previously ran 1.9.1; install/test compatible pinned environment rather than suppressing errors. **Mixed model availability:** filesystem presence != successful `joblib.load`. **422 feature mismatch:** inspect exact `feature_columns` then reconstruct lag/rolling features without future observations. **RAM pressure:** load one large RF at a time. **npm audit:** review advisories and test changes, avoid blind `--force`.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
