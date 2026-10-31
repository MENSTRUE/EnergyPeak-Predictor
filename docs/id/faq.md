# Faq — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Pertanyaan umum

**Apakah forecasting live?** Tidak, Forecast Explorer menampilkan evaluasi held-out historis. **Apakah 14/14 berarti 14 model bisa dimuat?** Tidak, itu hitungan file; loading perlu diuji terpisah. **Apakah tiga dataset digabung?** Tidak, eksperimen menjaga domain/interval. **Mengapa Peak F1?** Proksi event berbasis P90 train melengkapi MAE, bukan mengukur kondisi darurat jaringan. **Bolehkah forecast hanya dengan tanggal?** Tidak, estimator memerlukan fitur historis persis. **Apakah dataset asli disertakan?** Tidak, ambil sesuai hak dan provenance asal. **Apakah siap produksi?** Belum.

## Pemecahan masalah

**API offline:** jalankan backend di venv dan cek health. **CORS:** periksa `VITE_API_BASE_URL` dan origin backend. **404 metrics:** pulihkan CSV/JSON ke lokasi report tepat. **503 model hilang:** file `models/champion/{series_id}_champion.joblib` belum ada lokal. **503 `ModuleNotFoundError: _loss`:** artifact diserialisasi dengan scikit-learn 1.6.1 tetapi backend sempat memakai 1.9.1; pasang/uji environment terpin kompatibel, bukan menyembunyikan error. **Model sebagian berhasil:** file ada != `joblib.load` berhasil. **422 fitur tidak cocok:** periksa `feature_columns`, lalu rekonstruksi lag/rolling tanpa nilai masa depan. **RAM penuh:** muat RF besar satu per satu. **npm audit:** telaah advisory dan uji perubahan, hindari `--force` membabi buta.

## Cakupan dan batas klaim

Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
