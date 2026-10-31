# Reports — Dokumentasi Bahasa Indonesia

## Tujuan
Sumber: `reports/evaluation/{steel,appliances,electricity_MT_###}_heldout_metrics.json`. **Steel** (`random_forest_160`, 6.989 data test, kWh): MAE **3,9369**, RMSE **8,3710**, sMAPE **12,3215%**, Peak F1 **0,7314**, P90 train **83,74 kWh**. **Appliances** (`hist_gradient_boosting`, 3.928 data test, satuan energi asli dataset): MAE **25,3261**, RMSE **57,5269**, sMAPE **20,4713%**, Peak F1 **0,7117**. **Electricity MT_156** (`hist_gradient_boosting`, 28.032 data test, satuan asli): MAE **4,5920**, RMSE **6,5115**, sMAPE **5,7733%**, Peak F1 **0,9467**. Peak F1 memakai ambang P90 dari train dan tidak memvalidasi kegagalan jaringan secara independen. Jangan meranking MAE antarsatuan atau domain yang tidak sebanding.

## Batasan
Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Catatan teknis
Notebook membandingkan kandidat regresi termasuk baseline lag/musiman, hist-gradient boosting, dan `random_forest_160`. Setiap seri berdiri sendiri, tidak digabung antardomain. Kandidat ada di `reports/evaluation/*_validation_candidates.csv`, seluruh eksperimen di `reports/experiments/all_experiment_metrics.csv`. Pilih pemenang **hanya dari MAE validasi**, baru evaluasi test held-out sekali. Jangan memilih champion berdasarkan F1 test, MAE test, atau screenshot.

## Pengujian
Backend: `cd backend`, aktifkan venv Python, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; periksa `/docs` dan `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; buka `http://127.0.0.1:5173`. Uji integrasi manual: semua seri, pagination forecast dan empty state, schema model dan input 21 fitur yang sah, research gate, dan penanganan error. Screenshot membuktikan tampilan aplikasi lokal, bukan bukti seluruh rute/model lulus.

[README utama](../../README.md)
