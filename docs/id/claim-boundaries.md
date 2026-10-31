# Claim Boundaries — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Cakupan dan batas klaim

Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Keterbatasan dan ancaman validitas

Holdout kronologis bersifat internal, bukan validasi eksternal; perubahan musim atau rezim dapat menurunkan performa. Rekayasa fitur bergantung pada ketersediaan pengukuran, jendela warm-up, dan unit yang benar. Eksperimen Electricity mencakup 12 dari 370 pelanggan terpilih, bukan seluruhnya. Dataset rumah tangga berinterval 10 menit. Belum ada kalibrasi ketidakpastian, confidence interval, koneksi live, grid dispatch, penghematan tarif, atau jaminan operasional. Klasifikasi puncak berasal dari prediksi dan ambang, bukan label pemadaman yang diaudit terpisah.

## Lisensi dan hak data

Perangkat lunak repositori: MIT, lihat [`LICENSE`](LICENSE). Hak cipta 2026 Wafa Bila Syaefurokhman. Data UCI pihak ketiga, pengemasan Kaggle, gambar, serta dependency tetap mengikuti lisensi masing-masing. Verifikasi ketentuan penggunaan ulang sebelum mendistribusikan; jangan menganggap MIT otomatis berlaku pada dataset atau artifact yang dilatih darinya.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
