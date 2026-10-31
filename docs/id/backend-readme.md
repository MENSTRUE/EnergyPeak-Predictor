# Backend — Dokumentasi Bahasa Indonesia

## Tujuan
**Lapisan riset:** notebook Kaggle menghasilkan laporan dan artifact model. **API:** FastAPI menyajikan health, daftar seri, metrik tersimpan, sampel forecast berpaginasi, laporan audit/manifest, serta inspeksi/prediksi model bersyarat. **UI:** React + Vite + TypeScript menyediakan Overview, Forecast Explorer, Model Inference, Research & Audit. Laporan adalah snapshot read-only. `GET /api/v1/health`, `/api/v1/series`, `/api/v1/series/{series_id}/metrics`, `/api/v1/series/{series_id}/forecast`, `/api/v1/reports/model-manifest`, `/api/v1/reports/{name}`, `/api/v1/models/{series_id}`, `POST /api/v1/predict/{series_id}`. Inferensi membutuhkan joblib lokal tepercaya, fitur historis bernama persis, dan versi sklearn kompatibel.

## Batasan
Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Catatan teknis
`notebooks/` notebook master; `data/{raw,interim,processed,external}/` dataset lokal di-ignore; `models/{baseline,champion}/` artifact lokal (tidak masuk Git); `reports/{audit,evaluation,experiments,forecasts}/` hasil tersimpan; `assets/plots/` empat belas PNG forecast asli; `assets/screenshots/` empat tangkapan layar aplikasi; `backend/app/` FastAPI; `frontend/src/` React; `docs/{en,id}/` dokumentasi berpasangan; `scripts/` alat bantu; `tests/` pemeriksaan; `LICENSE` MIT. Lihat `docs/id/repository-map.md` untuk peta lengkap.

## Pengujian
Backend: `cd backend`, aktifkan venv Python, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; periksa `/docs` dan `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; buka `http://127.0.0.1:5173`. Uji integrasi manual: semua seri, pagination forecast dan empty state, schema model dan input 21 fitur yang sah, research gate, dan penanganan error. Screenshot membuktikan tampilan aplikasi lokal, bukan bukti seluruh rute/model lulus.

[README utama](../../README.md)
