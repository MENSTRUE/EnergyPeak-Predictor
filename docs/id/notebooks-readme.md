# Notebooks — Dokumentasi Bahasa Indonesia

## Tujuan
Puncak beban dapat relevan bagi perencanaan, tetapi grafik menarik bukan bukti forecast yang tepercaya. Tujuan terukur adalah memprediksi observasi berikutnya dari konteks historis yang benar-benar tersedia dan menilai apakah forecast melampaui **persentil ke-90 dari data train saja**. Regresi dan klasifikasi puncak turunan dilaporkan terpisah.

## Batasan
Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Catatan teknis
Setiap seri dibagi 60% train / 20% validasi / 20% test yang tidak disentuh, berdasarkan waktu tanpa shuffle. Seed: 42. Lag: `1,2,3,4,8,12,24,48,96`; rolling window: `4,12,48,96`; vektor kandidat memuat 21 fitur. Makna lag 96 tergantung interval: 24 jam pada data 15 menit, tetapi 16 jam pada data 10 menit. Pastikan rolling di-shift dan hanya memakai nilai sebelumnya, dan fitur kalender tersedia pada waktu prediksi.

## Pengujian
Backend: `cd backend`, aktifkan venv Python, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; periksa `/docs` dan `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; buka `http://127.0.0.1:5173`. Uji integrasi manual: semua seri, pagination forecast dan empty state, schema model dan input 21 fitur yang sah, research gate, dan penanganan error. Screenshot membuktikan tampilan aplikasi lokal, bukan bukti seluruh rute/model lulus.

[README utama](../../README.md)
