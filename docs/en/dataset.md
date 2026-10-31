# Dataset — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Dataset inventory and source provenance

**Primary — UCI Steel Industry Energy Consumption**: a single industrial facility; `Usage_kWh` target, 15-minute cadence. **Secondary — UCI ElectricityLoadDiagrams20112014**: 370 consumer streams available in the source; default notebook benchmarks 12 selected `MT_###` streams, each evaluated separately at 15-minute cadence, not the entire population. **Auxiliary — UCI Appliances Energy Prediction**: residential domain, `Appliances` target at 10-minute cadence. Dataset bundle observed in the Kaggle run at `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset`. Sources, filenames, intervals and roles are encoded in `reports/evaluation/source_provenance.csv`, `input_inventory.csv`. UCI dataset rights require checking source-specific terms; MIT software license does not relicense their data.

## Data audit and leakage controls

Inspect timestamp parsing, ordering, duplicates, missing intervals, outliers, units, series coverage, and minimum usable history. `research_gate.json` records PASS_REPRODUCIBILITY and flags chronological splits, training-only cutoffs, validation-only selection and source separation. This is an automated notebook gate, not external independent verification. Past-only features must be reconstructed at inference; do not let contemporaneous target or future exogenous observations slip into the input vector. Adjacent timestamps are autocorrelated even without exact duplicates.

## Chronological splitting and feature engineering

Each series uses 60% train / 20% validation / 20% untouched test, in time order and without shuffling. Run seed: 42. Configured lags: `1,2,3,4,8,12,24,48,96`; rolling windows: `4,12,48,96`; candidate vectors contain 21 features. The meaning of lag 96 depends on cadence: 24 hours for 15-minute data but 16 hours for 10-minute data. Confirm rolling is shifted and uses preceding measurements, and temporal fields reflect actual forecast-time availability.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
