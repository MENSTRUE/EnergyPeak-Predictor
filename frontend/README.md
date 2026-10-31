# EnergyPeak Predictor — Frontend

Research-oriented React/Vite/TypeScript user interface for the **Day 27/100 EnergyPeak Predictor** FastAPI backend.

## Before / Now / Next

- **Before:** notebook training, chronological splitting, source-separated experimental results, champion artifacts, held-out report generation.
- **Now:** present the actual saved Kaggle metrics, forecast samples, research gate, manifests, and guarded local model inference.
- **Next:** verify full data-contract compatibility and artifact feature schema; review visualizations against reports; conduct domain and near-duplicate audits, then consider production hardening separately.

## Setup (PowerShell)

From `D:\porto\100 day\day 27\EnergyPeak Predictor\frontend`:

```powershell
Copy-Item .env.example .env
npm install
npm run build
npm run dev
```

Open http://127.0.0.1:5173. Start backend on http://127.0.0.1:8000, with model files under `models/champion/` and reports under `reports/evaluation`, `reports/forecasts`, `reports/audit`.

`.env`:

```ini
VITE_API_BASE_URL=http://127.0.0.1:8000
```

The base URL is normalized, so `/api/v1` is not accidentally duplicated.

## Pages

1. **Overview:** live connectivity status and saved steel experiment metrics plus dataset-scoped research framing.
2. **Forecast Explorer:** saved held-out actual-vs-predicted line chart, paginated; MAE, RMSE, sMAPE, peak precision/recall/F1 and split sizes.
3. **Model Inference:** uses `/models/{series_id}` schema and requires all numeric features before submitting to `/predict/{series_id}`. Disabled if model or feature schema unavailable.
4. **Research & Audit:** read-only research gate, configurations, claim boundaries, electricity results, and model manifest.

## Contract

The implementation targets the companion **EnergyPeak_Day27_Full_FastAPI_Backend**: `/api/v1/health`, `/series`, `/series/{id}/metrics`, `/series/{id}/forecast`, `/reports/model-manifest`, `/reports/{name}`, `/models/{id}`, `/predict/{id}`. A model may be absent while reports remain available.

## Safety and validity

- This is a **research prototype**, not live grid data or automatic demand control.
- Metrics are held-out retrospective results; report rows are historical experiment records, not live forecasts.
- Never interpret a model prediction as an operational safety directive.
- Steel, household appliances, and electricity clients do **not** have comparable units without normalization and source-specific analysis.
- Peak labels derive from training P90 thresholds. No future target values should enter features.
- Remote/untrusted `.joblib` must never be loaded by the backend.

## Troubleshooting

- **API offline:** run `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000` inside `backend`, check `/api/v1/health` and CORS.
- **404 report:** ensure Kaggle JSON/CSV artifacts were placed in `reports/evaluation/`, `reports/forecasts/` and `reports/audit/`.
- **503 model:** copy trusted joblib from your Kaggle output to `models/champion` (not just `models/`).
- **Schema unavailable:** backend can only infer when the saved artifact exposes a trusted ordered feature list; do not guess field order.
- **TypeScript errors:** run `npm install` then `npm run build` and inspect diagnostics.

## Tests

`npm run typecheck` and `npm run build` check the frontend. Backend API tests are maintained separately. UI/API integration requires both services running.
