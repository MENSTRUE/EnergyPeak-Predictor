# Methodology — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Research problem and objective

Demand peaks may matter for planning, but an attractive chart is not a trustworthy forecast. The measurable objective is to predict the next observation using genuinely available historical context and evaluate whether forecasts exceed the **training-only 90th percentile**. Regression and derived peak classification are reported separately.

## Chronological splitting and feature engineering

Each series uses 60% train / 20% validation / 20% untouched test, in time order and without shuffling. Run seed: 42. Configured lags: `1,2,3,4,8,12,24,48,96`; rolling windows: `4,12,48,96`; candidate vectors contain 21 features. The meaning of lag 96 depends on cadence: 24 hours for 15-minute data but 16 hours for 10-minute data. Confirm rolling is shifted and uses preceding measurements, and temporal fields reflect actual forecast-time availability.

## Experiment design and champion selection

The notebook compares candidate regressors including seasonal/lag baselines, hist-gradient boosting and `random_forest_160`. Each series is treated independently, not concatenated across domains. Candidate comparisons live under `reports/evaluation/*_validation_candidates.csv`, full experiment records under `reports/experiments/all_experiment_metrics.csv`. Choose the winner **only by validation MAE**, then inspect a single held-out test result. No choosing a champion from test F1, test MAE, or screenshots.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
