# Data — EnergyPeak Predictor

## Purpose / Tujuan

**Primary — UCI Steel Industry Energy Consumption**: a single industrial facility; `Usage_kWh` target, 15-minute cadence. **Secondary — UCI ElectricityLoadDiagrams20112014**: 370 consumer streams available in the source; default notebook benchmarks 12 selected `MT_###` streams, each evaluated separately at 15-minute cadence, not the entire population. **Auxiliary — UCI Appliances Energy Prediction**: residential domain, `Appliances` target at 10-minute cadence. Dataset bundle observed in the Kaggle run at `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset`. Sources, filenames, intervals and roles are encoded in `reports/evaluation/source_provenance.csv`, `input_inventory.csv`. UCI dataset rights require checking source-specific terms; MIT software license does not relicense their data.

## Scientific safeguards

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Technical notes

Inspect timestamp parsing, ordering, duplicates, missing intervals, outliers, units, series coverage, and minimum usable history. `research_gate.json` records PASS_REPRODUCIBILITY and flags chronological splits, training-only cutoffs, validation-only selection and source separation. This is an automated notebook gate, not external independent verification. Past-only features must be reconstructed at inference; do not let contemporaneous target or future exogenous observations slip into the input vector. Adjacent timestamps are autocorrelated even without exact duplicates.

## Validation

Backend: `cd backend`, activate Python virtual environment, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; check `/docs` and `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; inspect `http://127.0.0.1:5173`. Manual integration: exercise each series, forecast pagination and empty states, model schema and a legitimate 21-feature input, research gate and error handling. Screenshots show local application views, not proof all routes/models pass.

## Reference / Rujukan

[Root README](../README.md) · [Indonesian README](../docs/id/README.md)
