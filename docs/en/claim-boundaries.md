# Claim Boundaries — EnergyPeak Predictor

This document expands the corresponding source-of-truth sections in the root README. All figures and limitations refer to saved repository outputs.

## Scope and claim boundaries

Supported: within-series, one-step-ahead retrospective evaluation, saved Kaggle metrics, trained champion selection on validation MAE, threshold-derived peak indicators. Unsupported: real-time IoT sensing, day-ahead dispatch, tariff/cost savings, peak guarantees, generic forecasts from timestamp alone, grid actuation or validated external generalization. Never equate model presence with successful deserialization or prediction readiness.

## Limitations and threats to validity

Chronological holdout is internal, not external validation; seasonal/regime shifts may invalidate historical performance. Feature engineering depends on measurement availability, warm-up windows and correct units. Electricity experiment covers selected 12 of 370 clients, not every customer. The residential dataset uses 10-minute intervals. No uncertainty calibration, confidence intervals, live connectivity, grid dispatch, tariff savings or operational guarantee. Peak classification derives from predictions and threshold, not separately audited outage labels.

## License and data rights

Repository software: MIT, see [`LICENSE`](LICENSE). Copyright 2026 Wafa Bila Syaefurokhman. Third-party UCI data, Kaggle packaging, images and other dependencies retain their respective licenses. Verify dataset reuse terms before redistribution; do not assume MIT covers the datasets or trained artifacts from them.

## Evidence paths

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
