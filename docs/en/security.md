# Security — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Local deployment and production checklist

Local-first. Store trusted champions in `models/champion/` and reports in committed `reports/`. Keep `.env` secret, set narrowly scoped CORS origins, and limit network binding to localhost during research. Before internet-facing deployment require authentication, request throttling, HTTPS, resource budgets, security tests, monitoring and source-data permissions; large Random Forest artifacts can consume hundreds of MB each. No production validation is claimed.

## Limitations and threats to validity

Chronological holdout is internal, not external validation; seasonal/regime shifts may invalidate historical performance. Feature engineering depends on measurement availability, warm-up windows and correct units. Electricity experiment covers selected 12 of 370 clients, not every customer. The residential dataset uses 10-minute intervals. No uncertainty calibration, confidence intervals, live connectivity, grid dispatch, tariff savings or operational guarantee. Peak classification derives from predictions and threshold, not separately audited outage labels.

## Scope and claim boundaries

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
