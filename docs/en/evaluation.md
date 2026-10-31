# Evaluation — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Held-out evaluation metrics

Source: `reports/evaluation/{steel,appliances,electricity_MT_###}_heldout_metrics.json`. **Steel** (`random_forest_160`, 6,989 test rows, kWh): MAE **3.9369**, RMSE **8.3710**, sMAPE **12.3215%**, Peak F1 **0.7314**, training P90 **83.74 kWh**. **Appliances** (`hist_gradient_boosting`, 3,928 test rows, source-original energy units): MAE **25.3261**, RMSE **57.5269**, sMAPE **20.4713%**, Peak F1 **0.7117**. **Electricity MT_156** (`hist_gradient_boosting`, 28,032 test rows, source-original units): MAE **4.5920**, RMSE **6.5115**, sMAPE **5.7733%**, Peak F1 **0.9467**. Peak F1 uses a threshold set on train P90 and does not independently validate grid failures. Do not rank MAE across incomparable target units or domains.

## Experiment design and champion selection

The notebook compares candidate regressors including seasonal/lag baselines, hist-gradient boosting and `random_forest_160`. Each series is treated independently, not concatenated across domains. Candidate comparisons live under `reports/evaluation/*_validation_candidates.csv`, full experiment records under `reports/experiments/all_experiment_metrics.csv`. Choose the winner **only by validation MAE**, then inspect a single held-out test result. No choosing a champion from test F1, test MAE, or screenshots.

## Limitations and threats to validity

Chronological holdout is internal, not external validation; seasonal/regime shifts may invalidate historical performance. Feature engineering depends on measurement availability, warm-up windows and correct units. Electricity experiment covers selected 12 of 370 clients, not every customer. The residential dataset uses 10-minute intervals. No uncertainty calibration, confidence intervals, live connectivity, grid dispatch, tariff savings or operational guarantee. Peak classification derives from predictions and threshold, not separately audited outage labels.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
