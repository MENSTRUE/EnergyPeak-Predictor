# Roadmap — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Before — Now — Next

**Before:** audited three UCI-source datasets; created lag/rolling features from past observations; chronological splits; trained candidate models and selected each champion on validation MAE; exported held-out metrics, forecasts, plots, model manifest and 14 champions. **Now:** repository publishes notebook, reports, 14 plots, 4 screenshots and full-stack prototype; the local UI has shown API connected and historical data, while model loading has exposed an environment mismatch. **Next:** pin a verified compatible inference environment, test full 21-feature vectors, validate every route, run independent domain drift and near-duplicate checks, and only then consider controlled deployment.

## Roadmap

**P0:** compatible joblib environment and model smoke tests across all 14 series; verify each exact feature vector. **P1:** automated end-to-end report/plot consistency tests, runtime API/UI checks and provenance/hashes. **P2:** rolling-origin and seasonal robustness, near-duplicate investigation, unseen-series/domain drift checks. **P3:** bounded input orchestration and guarded pilot; no automatic energy control without independent operational studies.

## FAQ

**Is this live forecasting?** No, the displayed forecast explorer is historical held-out evaluation. **Does 14/14 mean 14 models load?** No, it counts files; loading must be tested separately. **Are the three datasets fused?** No, experiments preserve domain and cadence. **Why Peak F1?** A train-P90 event proxy complements MAE; it does not measure grid emergency. **Can I forecast using date only?** No, saved estimators require exact historical features. **Is the source data included?** No, fetch it subject to its original rights and provenance. **Is the software production-ready?** No.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
