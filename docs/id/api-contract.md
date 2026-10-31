# Api Contract — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Arsitektur aplikasi dan API

**Lapisan riset:** notebook Kaggle menghasilkan laporan dan artifact model. **API:** FastAPI menyajikan health, daftar seri, metrik tersimpan, sampel forecast berpaginasi, laporan audit/manifest, serta inspeksi/prediksi model bersyarat. **UI:** React + Vite + TypeScript menyediakan Overview, Forecast Explorer, Model Inference, Research & Audit. Laporan adalah snapshot read-only. `GET /api/v1/health`, `/api/v1/series`, `/api/v1/series/{series_id}/metrics`, `/api/v1/series/{series_id}/forecast`, `/api/v1/reports/model-manifest`, `/api/v1/reports/{name}`, `/api/v1/models/{series_id}`, `POST /api/v1/predict/{series_id}`. Inferensi membutuhkan joblib lokal tepercaya, fitur historis bernama persis, dan versi sklearn kompatibel.

## Pengujian backend dan frontend

Backend: `cd backend`, aktifkan venv Python, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; periksa `/docs` dan `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; buka `http://127.0.0.1:5173`. Uji integrasi manual: semua seri, pagination forecast dan empty state, schema model dan input 21 fitur yang sah, research gate, dan penanganan error. Screenshot membuktikan tampilan aplikasi lokal, bukan bukti seluruh rute/model lulus.

## Pemecahan masalah

**API offline:** jalankan backend di venv dan cek health. **CORS:** periksa `VITE_API_BASE_URL` dan origin backend. **404 metrics:** pulihkan CSV/JSON ke lokasi report tepat. **503 model hilang:** file `models/champion/{series_id}_champion.joblib` belum ada lokal. **503 `ModuleNotFoundError: _loss`:** artifact diserialisasi dengan scikit-learn 1.6.1 tetapi backend sempat memakai 1.9.1; pasang/uji environment terpin kompatibel, bukan menyembunyikan error. **Model sebagian berhasil:** file ada != `joblib.load` berhasil. **422 fitur tidak cocok:** periksa `feature_columns`, lalu rekonstruksi lag/rolling tanpa nilai masa depan. **RAM penuh:** muat RF besar satu per satu. **npm audit:** telaah advisory dan uji perubahan, hindari `--force` membabi buta.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
