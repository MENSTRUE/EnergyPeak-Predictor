# Visual Evidence — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Bukti visual — screenshot dan semua plot

Empat belas gambar forecast di repositori memperlihatkan nilai aktual versus prediksi held-out untuk Steel, Appliances dan dua belas seri konsumen Electricity yang dievaluasi terpisah. Empat screenshot UI memperlihatkan konsol riset; plot maupun screenshot tidak membuktikan performa live atau kesiapan loading model.

![steel forecast](../../assets/plots/steel_test_forecast.png)
![appliances forecast](../../assets/plots/appliances_test_forecast.png)
![electricity_MT_156 forecast](../../assets/plots/electricity_MT_156_test_forecast.png)
![electricity_MT_158 forecast](../../assets/plots/electricity_MT_158_test_forecast.png)
![electricity_MT_159 forecast](../../assets/plots/electricity_MT_159_test_forecast.png)
![electricity_MT_166 forecast](../../assets/plots/electricity_MT_166_test_forecast.png)
![electricity_MT_168 forecast](../../assets/plots/electricity_MT_168_test_forecast.png)
![electricity_MT_169 forecast](../../assets/plots/electricity_MT_169_test_forecast.png)
![electricity_MT_171 forecast](../../assets/plots/electricity_MT_171_test_forecast.png)
![electricity_MT_172 forecast](../../assets/plots/electricity_MT_172_test_forecast.png)
![electricity_MT_176 forecast](../../assets/plots/electricity_MT_176_test_forecast.png)
![electricity_MT_180 forecast](../../assets/plots/electricity_MT_180_test_forecast.png)
![electricity_MT_182 forecast](../../assets/plots/electricity_MT_182_test_forecast.png)
![electricity_MT_183 forecast](../../assets/plots/electricity_MT_183_test_forecast.png)
![UI 1](../../assets/screenshots/Screenshot%202026-10-31%20141604.png)
![UI 2](../../assets/screenshots/Screenshot%202026-10-31%20141628.png)
![UI 3](../../assets/screenshots/Screenshot%202026-10-31%20141643.png)
![UI 4](../../assets/screenshots/Screenshot%202026-10-31%20141657.png)

## Berkas sumber kebenaran

Hasil numerik: `reports/evaluation/*_heldout_metrics.json`; kandidat validasi: `reports/evaluation/*_validation_candidates.csv`; inventaris eksperimen: `reports/experiments/all_experiment_metrics.csv`; CSV prediksi historis: `reports/forecasts/*_heldout_predictions.csv`; manifest champion: `reports/audit/model_manifest.csv`; konfigurasi: `reports/evaluation/run_config.json`; batas klaim: `reports/evaluation/claim_boundaries.json`; gerbang kesiapan: `reports/evaluation/research_gate.json`; asal data: `reports/evaluation/source_provenance.csv`; kode: `notebooks/energypeak-predictor.ipynb`, `backend/app/`, `frontend/src/`. README adalah indeks, bukan pengganti artifact data ini.

## Metrik evaluasi held-out

Sumber: `reports/evaluation/{steel,appliances,electricity_MT_###}_heldout_metrics.json`. **Steel** (`random_forest_160`, 6.989 data test, kWh): MAE **3,9369**, RMSE **8,3710**, sMAPE **12,3215%**, Peak F1 **0,7314**, P90 train **83,74 kWh**. **Appliances** (`hist_gradient_boosting`, 3.928 data test, satuan energi asli dataset): MAE **25,3261**, RMSE **57,5269**, sMAPE **20,4713%**, Peak F1 **0,7117**. **Electricity MT_156** (`hist_gradient_boosting`, 28.032 data test, satuan asli): MAE **4,5920**, RMSE **6,5115**, sMAPE **5,7733%**, Peak F1 **0,9467**. Peak F1 memakai ambang P90 dari train dan tidak memvalidasi kegagalan jaringan secara independen. Jangan meranking MAE antarsatuan atau domain yang tidak sebanding.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
