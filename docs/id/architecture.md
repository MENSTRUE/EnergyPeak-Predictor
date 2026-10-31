# Architecture — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Arsitektur aplikasi dan API

**Lapisan riset:** notebook Kaggle menghasilkan laporan dan artifact model. **API:** FastAPI menyajikan health, daftar seri, metrik tersimpan, sampel forecast berpaginasi, laporan audit/manifest, serta inspeksi/prediksi model bersyarat. **UI:** React + Vite + TypeScript menyediakan Overview, Forecast Explorer, Model Inference, Research & Audit. Laporan adalah snapshot read-only. `GET /api/v1/health`, `/api/v1/series`, `/api/v1/series/{series_id}/metrics`, `/api/v1/series/{series_id}/forecast`, `/api/v1/reports/model-manifest`, `/api/v1/reports/{name}`, `/api/v1/models/{series_id}`, `POST /api/v1/predict/{series_id}`. Inferensi membutuhkan joblib lokal tepercaya, fitur historis bernama persis, dan versi sklearn kompatibel.

## Struktur repositori

`notebooks/` notebook master; `data/{raw,interim,processed,external}/` dataset lokal di-ignore; `models/{baseline,champion}/` artifact lokal (tidak masuk Git); `reports/{audit,evaluation,experiments,forecasts}/` hasil tersimpan; `assets/plots/` empat belas PNG forecast asli; `assets/screenshots/` empat tangkapan layar aplikasi; `backend/app/` FastAPI; `frontend/src/` React; `docs/{en,id}/` dokumentasi berpasangan; `scripts/` alat bantu; `tests/` pemeriksaan; `LICENSE` MIT. Lihat `docs/id/repository-map.md` untuk peta lengkap.

## Cakupan dan batas klaim

Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
