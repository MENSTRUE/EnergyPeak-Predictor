# Docs — EnergyPeak Predictor

## Purpose / Tujuan

`notebooks/` research master; `data/{raw,interim,processed,external}/` ignored local datasets; `models/{baseline,champion}/` local artifacts (not committed); `reports/{audit,evaluation,experiments,forecasts}/` saved results; `assets/plots/` fourteen real forecast PNGs; `assets/screenshots/` four app captures; `backend/app/` FastAPI; `frontend/src/` React; `docs/{en,id}/` paired documentation; `scripts/` helpers; `tests/` checks; `LICENSE` MIT. See `docs/en/repository-map.md` for a fuller map.

## Scientific safeguards

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Technical notes

Numerical results: `reports/evaluation/*_heldout_metrics.json`; detailed validation candidate comparisons: `reports/evaluation/*_validation_candidates.csv`; experiment inventory: `reports/experiments/all_experiment_metrics.csv`; historical forecast CSV: `reports/forecasts/*_heldout_predictions.csv`; champion manifest: `reports/audit/model_manifest.csv`; methodology configuration: `reports/evaluation/run_config.json`; constraints: `reports/evaluation/claim_boundaries.json`; readiness gate: `reports/evaluation/research_gate.json`; exact source attribution: `reports/evaluation/source_provenance.csv`; code: `notebooks/energypeak-predictor.ipynb`, `backend/app/`, `frontend/src/`. This README is an index, not a replacement for these data artifacts.

## Validation

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Reference / Rujukan

[Root README](../README.md) · [Indonesian README](../docs/id/README.md)
