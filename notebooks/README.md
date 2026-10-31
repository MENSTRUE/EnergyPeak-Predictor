# Notebooks — EnergyPeak Predictor

## Purpose / Tujuan

Demand peaks may matter for planning, but an attractive chart is not a trustworthy forecast. The measurable objective is to predict the next observation using genuinely available historical context and evaluate whether forecasts exceed the **training-only 90th percentile**. Regression and derived peak classification are reported separately.

## Scientific safeguards

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Technical notes

Each series uses 60% train / 20% validation / 20% untouched test, in time order and without shuffling. Run seed: 42. Configured lags: `1,2,3,4,8,12,24,48,96`; rolling windows: `4,12,48,96`; candidate vectors contain 21 features. The meaning of lag 96 depends on cadence: 24 hours for 15-minute data but 16 hours for 10-minute data. Confirm rolling is shifted and uses preceding measurements, and temporal fields reflect actual forecast-time availability.

## Validation

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Reference / Rujukan

[Root README](../README.md) · [Indonesian README](../docs/id/README.md)
