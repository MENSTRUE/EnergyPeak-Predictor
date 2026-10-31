# Security — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Deployment lokal dan daftar kesiapan produksi

Utamakan lokal. Simpan champion tepercaya di `models/champion/` dan laporan di `reports/` yang dilacak Git. Rahasiakan `.env`, batasi CORS, dan bind server ke localhost selama riset. Sebelum deployment internet dibutuhkan autentikasi, rate limiting, HTTPS, anggaran resource, uji keamanan, monitoring, dan izin sumber data; Random Forest besar dapat memakai ratusan MB per model. Tidak ada klaim validasi produksi.

## Keterbatasan dan ancaman validitas

Holdout kronologis bersifat internal, bukan validasi eksternal; perubahan musim atau rezim dapat menurunkan performa. Rekayasa fitur bergantung pada ketersediaan pengukuran, jendela warm-up, dan unit yang benar. Eksperimen Electricity mencakup 12 dari 370 pelanggan terpilih, bukan seluruhnya. Dataset rumah tangga berinterval 10 menit. Belum ada kalibrasi ketidakpastian, confidence interval, koneksi live, grid dispatch, penghematan tarif, atau jaminan operasional. Klasifikasi puncak berasal dari prediksi dan ambang, bukan label pemadaman yang diaudit terpisah.

## Cakupan dan batas klaim

Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
