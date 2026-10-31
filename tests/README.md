# Tests — EnergyPeak Predictor

## Purpose / Tujuan

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Scientific safeguards

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Technical notes

Local-first. Store trusted champions in `models/champion/` and reports in committed `reports/`. Keep `.env` secret, set narrowly scoped CORS origins, and limit network binding to localhost during research. Before internet-facing deployment require authentication, request throttling, HTTPS, resource budgets, security tests, monitoring and source-data permissions; large Random Forest artifacts can consume hundreds of MB each. No production validation is claimed.

## Validation

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Reference / Rujukan

[Root README](../README.md) · [Indonesian README](../docs/id/README.md)
