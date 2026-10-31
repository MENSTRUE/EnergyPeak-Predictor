# Reproducibility — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Berkas sumber kebenaran

Hasil numerik: `reports/evaluation/*_heldout_metrics.json`; kandidat validasi: `reports/evaluation/*_validation_candidates.csv`; inventaris eksperimen: `reports/experiments/all_experiment_metrics.csv`; CSV prediksi historis: `reports/forecasts/*_heldout_predictions.csv`; manifest champion: `reports/audit/model_manifest.csv`; konfigurasi: `reports/evaluation/run_config.json`; batas klaim: `reports/evaluation/claim_boundaries.json`; gerbang kesiapan: `reports/evaluation/research_gate.json`; asal data: `reports/evaluation/source_provenance.csv`; kode: `notebooks/energypeak-predictor.ipynb`, `backend/app/`, `frontend/src/`. README adalah indeks, bukan pengganti artifact data ini.

## Reproduksibilitas dan eksekusi

Input riset: `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset`; gunakan `notebooks/energypeak-predictor.ipynb`. Konfigurasi mencatat Python Kaggle **3.13.15** dan seed **42**; jangan menganggap versi Python notebook dan Windows lokal sama. Catat versi pandas, NumPy, scikit-learn, joblib, serta versi ekspor artifact sebelum menjalankan ulang. Sumber dapat diaudit melalui `source_provenance.csv`, `input_inventory.csv`, `run_config.json`, `research_gate.json`. Hasil ulang harus dibandingkan berdasarkan metrik dan hash agar bisa disebut reproduksi; status PASS saja tidak cukup.

## Audit data dan kontrol kebocoran

Periksa parsing/urutan timestamp, duplikasi, interval hilang, outlier, unit, cakupan seri, dan riwayat minimum yang bisa dipakai. `research_gate.json` merekam PASS_REPRODUCIBILITY serta penanda split kronologis, ambang dari train, seleksi validasi, dan pemisahan sumber. Ini gerbang otomatis notebook, bukan verifikasi independen eksternal. Fitur masa lalu wajib direkonstruksi saat inferensi; jangan memasukkan target saat ini atau variabel eksogen masa depan. Timestamp berdekatan tetap berkorelasi meski tidak ada duplikat identik.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
