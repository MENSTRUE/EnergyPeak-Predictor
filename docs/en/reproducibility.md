# Reproducibility — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Source-of-truth files

Numerical results: `reports/evaluation/*_heldout_metrics.json`; detailed validation candidate comparisons: `reports/evaluation/*_validation_candidates.csv`; experiment inventory: `reports/experiments/all_experiment_metrics.csv`; historical forecast CSV: `reports/forecasts/*_heldout_predictions.csv`; champion manifest: `reports/audit/model_manifest.csv`; methodology configuration: `reports/evaluation/run_config.json`; constraints: `reports/evaluation/claim_boundaries.json`; readiness gate: `reports/evaluation/research_gate.json`; exact source attribution: `reports/evaluation/source_provenance.csv`; code: `notebooks/energypeak-predictor.ipynb`, `backend/app/`, `frontend/src/`. This README is an index, not a replacement for these data artifacts.

## Reproducibility and execution

Input root: `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset` at research time; use `notebooks/energypeak-predictor.ipynb`. Run config records Kaggle Python **3.13.15** and seed **42**; do not assume that notebook Python and local Windows Python match. Record pandas, NumPy, scikit-learn, joblib and model export versions before re-running. Source is auditable through `source_provenance.csv`, `input_inventory.csv`, `run_config.json`, `research_gate.json`. Outputs need comparison via metrics and hashes to call a rerun reproduced; a PASS gate alone is insufficient.

## Data audit and leakage controls

Inspect timestamp parsing, ordering, duplicates, missing intervals, outliers, units, series coverage, and minimum usable history. `research_gate.json` records PASS_REPRODUCIBILITY and flags chronological splits, training-only cutoffs, validation-only selection and source separation. This is an automated notebook gate, not external independent verification. Past-only features must be reconstructed at inference; do not let contemporaneous target or future exogenous observations slip into the input vector. Adjacent timestamps are autocorrelated even without exact duplicates.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
