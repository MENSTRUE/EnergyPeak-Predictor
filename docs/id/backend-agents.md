# Aturan agen backend — EnergyPeak Predictor

# EnergyPeak Predictor — AGENTS.md (Bahasa Indonesia)

## Kontrak wajib
Repo adalah prototipe penelitian ilmiah, bukan pengendali jaringan listrik live. Dilarang mengarang eksperimen, benchmark, output model, keberhasilan deployment, lisensi data, atau manfaat operasional. Dasarkan perubahan pada berkas nyata; sebut path laporan dan satuan tepat. `README.md` adalah indeks sumber kebenaran; angka berasal dari JSON/CSV Kaggle, bukan dari narasi.

## Alur Before–Now–Next
**Sebelum:** inventaris repo/sumber dan baca batas klaim; **Sekarang:** ubah dalam cakupan terkontrol serta uji; **Berikutnya:** laporkan hasil tes/keterbatasan, perbarui dokumen EN/ID, berikan pesan commit standar. Jangan mengubah split evaluasi atau seleksi champion diam-diam.

## Aturan riset keras
1. Split kronologis train/validasi/test 60/20/20 tanpa shuffle. MAE validasi memilih champion; test held-out setelah seleksi.
2. Semua fitur lag/rolling hanya dari target sebelumnya. Ambang puncak adalah P90 train. Hormati interval dan satuan asli.
3. Jangan menyatukan Steel, Electricity, Appliances ke satu populasi target; 12 seri Electricity terpilih bukan evaluasi 370 pelanggan.
4. CSV historis harus dilabeli saved/retrospective. API connected != model berhasil dimuat; file ada != prediksi siap.
5. Jangan membuat 21 nilai fitur hanya dari timestamp. Ikuti `feature_columns`, transformasi, dan ketersediaan data.
6. Dilarang mengklaim kontrol listrik live, penghematan biaya, jaminan cegah puncak, kalibrasi ketidakpastian, atau keselamatan.
7. Jangan memuat joblib tidak tepercaya; cocokkan sklearn (artifact 1.6.1 dan backend 1.9.1 pernah menyebabkan error `_loss`). Batasi unpickling dan RAM.
8. Dataset mentah dan model besar jangan dikomit ke Git. Simpan log, konfigurasi, provenance dan limitation.
9. Dilarang membuat grafik, screenshot, atau angka rekaan. Semua path aset harus ada.
10. Setiap perubahan Markdown wajib memperbarui pasangan EN dan ID secara penuh; terjemahan tidak boleh meringkas atau melemahkan batas klaim.

## Protokol perubahan API/aplikasi
Periksa `backend/app/api/routes/`, `frontend/src/services/api.ts`, `frontend/src/types/api.ts` sebelum mengubah route. Perbarui dua sisi serentak; jangan gandakan `/api/v1`. Pertahankan error 503/422 secara jelas.

## Verifikasi
Backend `python -m pytest -q`; frontend `npm run build`; manual: health, series, metrics, forecasts, manifest, model loading, feature input, Research & Audit. Tes yang belum dijalankan harus disebutkan.

## Definisi selesai
Output ter-grounding; sumber berversi; command reproduksi; tanpa secret; path aset valid; EN/ID setara; batas klaim utuh; hasil uji dilaporkan jujur.

## Khusus backend
Jangan menyatakan model siap sebelum joblib berhasil dimuat, schema terurut tersedia, dan smoke inference lulus. Jangan menyembunyikan exception asli saat diagnosis.
