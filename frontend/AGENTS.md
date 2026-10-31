# Frontend AGENTS — EnergyPeak Predictor

# EnergyPeak Predictor — AGENTS.md

## Mandatory operating contract
This repository is a scientific research prototype, not a live electricity controller. Do not fabricate experiments, benchmarks, model outputs, deployment success, data licensing or operational benefit. Work from actual files, cite exact report paths and use precise units. Root `README.md` is the navigation source-of-truth; raw numbers come from Kaggle JSON/CSV files, not prose.

## Workflow / Before–Now–Next
**Before:** inventory repo + sources and read claim boundaries; **Now:** make scoped, tested changes; **Next:** report tests, limitations, update EN/ID documentation, propose a conventional commit. Never silently alter evaluation splits or champion selection.

## Hard research rules
1. Train/validation/test by chronology 60/20/20, no random shuffling of time points. Validation MAE chooses champion; held-out test read afterward.
2. All lag/rolling features use prior observed targets only. Peak threshold is train P90. Preserve cadence-specific semantics and original units.
3. Never fuse Steel, Electricity, and Appliances into one target population; 12 selected Electricity streams are not 370-client benchmark evidence.
4. Historical CSVs must be labeled saved/retrospective. API connected != model loaded. Artifact present != predictor ready.
5. Do not infer a 21-value feature vector from timestamp only. Honor exact `feature_columns`, transform conventions and source data availability.
6. No live demand response, grid control, savings, guaranteed peak prevention, calibrated uncertainty or safety claims.
7. Do not load untrusted `.joblib` files; align scikit-learn version (observed artifact 1.6.1; incompatible backend 1.9.1 caused `_loss` error). Limit unpickling and model memory.
8. Keep source datasets and large artifacts out of Git. Preserve logs, configs, provenance, reporting and scientific limitations.
9. No manufactured charts, screenshots or scores. Asset references must resolve to tracked files.
10. Every Markdown modification must update the complete EN and ID counterpart; translation must not shorten or weaken caveats.

## API / app change protocol
Check `backend/app/api/routes/`, `frontend/src/services/api.ts`, `frontend/src/types/api.ts` before changing routes. Update both sides atomically. Ensure `/api/v1` is not doubled. Keep error codes and 503/422 states visible.

## Verification
Backend: `python -m pytest -q`; frontend: `npm run build`; manual: health, series, metrics, forecasts, manifest, model loading, feature vectors, Research & Audit. Document unrun tests explicitly.

## Definition of done
Grounded result; versioned source; reproducing command; no security secrets; all asset paths verified; EN/ID parity; claim-boundaries intact; test results accurately disclosed.

## Frontend-specific rule
Keep research caveats visible, use real series IDs, never turn file presence into inference readiness, and render 503/422 errors. Chart actual/predicted rows must remain labeled historical held-out data.
