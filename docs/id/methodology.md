# Methodology — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Masalah dan tujuan penelitian

Puncak beban dapat relevan bagi perencanaan, tetapi grafik menarik bukan bukti forecast yang tepercaya. Tujuan terukur adalah memprediksi observasi berikutnya dari konteks historis yang benar-benar tersedia dan menilai apakah forecast melampaui **persentil ke-90 dari data train saja**. Regresi dan klasifikasi puncak turunan dilaporkan terpisah.

## Pembagian kronologis dan rekayasa fitur

Setiap seri dibagi 60% train / 20% validasi / 20% test yang tidak disentuh, berdasarkan waktu tanpa shuffle. Seed: 42. Lag: `1,2,3,4,8,12,24,48,96`; rolling window: `4,12,48,96`; vektor kandidat memuat 21 fitur. Makna lag 96 tergantung interval: 24 jam pada data 15 menit, tetapi 16 jam pada data 10 menit. Pastikan rolling di-shift dan hanya memakai nilai sebelumnya, dan fitur kalender tersedia pada waktu prediksi.

## Desain eksperimen dan pemilihan champion

Notebook membandingkan kandidat regresi termasuk baseline lag/musiman, hist-gradient boosting, dan `random_forest_160`. Setiap seri berdiri sendiri, tidak digabung antardomain. Kandidat ada di `reports/evaluation/*_validation_candidates.csv`, seluruh eksperimen di `reports/experiments/all_experiment_metrics.csv`. Pilih pemenang **hanya dari MAE validasi**, baru evaluasi test held-out sekali. Jangan memilih champion berdasarkan F1 test, MAE test, atau screenshot.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
