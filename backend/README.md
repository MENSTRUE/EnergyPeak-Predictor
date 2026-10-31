# EnergyPeak Predictor — FastAPI research backend

Real read-only Kaggle evaluation snapshots and optional **explicit-feature** artifact inference. Nothing in this backend monitors the electricity grid, and the API **does not** forecast from timestamp alone. No data, prediction, test metric, or confidence value is fabricated.

## Confirmed repository layout

The Kaggle run saved metrics under `reports/evaluation/*_heldout_metrics.json` (each a JSON list with one result), historical prediction rows under `reports/forecasts/*_heldout_predictions.csv`, and a model manifest under `reports/audit/model_manifest.csv`. The manifest lists 14 series and champion artifacts. Models in `models/champion/` are intentionally ignored by git by default and must be placed on the operator's machine.

## Local installation — Windows PowerShell

```powershell
cd "D:\porto\100 day\day 27\EnergyPeak Predictor\backend"
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and `/api/v1/health`. Run tests via `python -m pytest -q`.

## Endpoints

| Endpoint | Purpose |
| --- | --- |
| `GET /api/v1/health` | API and artifact presence, never a readiness guarantee |
| `GET /api/v1/series` | IDs discovered from saved report filenames |
| `GET /api/v1/series/{series_id}/metrics` | Actual held-out metrics as recorded by Kaggle |
| `GET /api/v1/series/{series_id}/forecast?limit=100&offset=0` | Read-only held-out prediction rows |
| `GET /api/v1/reports/model-manifest` | Champion model manifest CSV |
| `GET /api/v1/reports/research_gate` | Research gate JSON |
| `GET /api/v1/reports/run_config` | Split and lag configuration |
| `GET /api/v1/reports/claim_boundaries` | Approved claims and limitations |
| `GET /api/v1/reports/electricity_results` | Electricity study summary |
| `GET /api/v1/models/{series_id}` | Inspect local serialized artifact and feature contract |
| `POST /api/v1/predict/{series_id}` | Optional one-step model inference from named historical features |

`POST /api/v1/predict/steel` accepts `{"features":{"exact_feature_name":123.0,...}}`. First use `GET /api/v1/models/steel` to inspect required names. Every required feature must be supplied; missing or extra features return 422. If Kaggle export does not include a usable estimator or feature names, this endpoint correctly refuses inference rather than guessing feature semantics.

## Important: joblib export contract

Model files may be a direct scikit-learn estimator or dictionaries holding the estimator in `model`, `pipeline`, or `estimator` and optional `feature_columns`/`feature_names`. If a saved model uses a different schema, extend the loader **after inspecting the trusted artifact**, and add a test. Do **not** deserialize foreign joblib files. Always align the scikit-learn version to the training environment.

## Scientific limits

These are research estimates from chronological 60/20/20 splits, with champion selection on validation and test held out. Steel, household appliances, and per-consumer Electricity are separate domains, with differing target units. Do not compare raw MAE across domains as if units match. Peak cutoffs are defined from the training partition. Evaluation reports are historical, not live prediction or safety/operational decisions. Real forecast inference requires exact lag, rolling and timestamp feature availability from past observations only. Feature order, transformations, and sampling interval must match Kaggle. UI should label forecast CSV as **held-out historical evaluation**.

## Deployment and security

Run locally by default. Before public deployment: authentication, rate limiting, secure ingress/TLS, request budgets, monitoring, explicit CORS domains and model provenance are required. Large random-forest `.joblib` files can use substantial RAM. Avoid loading all champions simultaneously.

## Troubleshooting

- **404 metrics:** copy the exact `reports/evaluation/` files from Kaggle into repo.
- **503 missing model:** supply the expected `.joblib` in `models/champion/`; this is optional for reports.
- **422 feature mismatch:** call model inspection and submit every exact feature name, after reconstructing the original preprocessing.
- **503 artifact load:** Python/scikit-learn versions may differ; re-export in a pinned environment.
- **CORS:** set `ENERGYPEAK_CORS_ORIGINS` and restart.
- **Large report:** use `limit` and `offset` pagination; default cap is 500 rows.
