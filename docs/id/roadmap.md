# Roadmap — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Sebelum — Sekarang — Berikutnya

**Sebelum:** mengaudit tiga dataset bersumber dari UCI; membuat fitur lag/rolling hanya dari observasi masa lalu; membagi data kronologis; melatih kandidat dan memilih champion tiap seri memakai MAE validasi; mengekspor metrik held-out, forecast, plot, manifest, dan 14 champion. **Sekarang:** repositori memublikasikan notebook, laporan, 14 plot, 4 screenshot serta prototipe full-stack; UI lokal sudah memperlihatkan API connected dan data historis, sedangkan loading model menemukan ketidakcocokan environment. **Berikutnya:** kunci environment inferensi yang kompatibel dan teruji, uji vektor 21 fitur, validasi semua endpoint, audit drift domain dan near-duplicate, baru pertimbangkan deployment terbatas.

## Peta jalan

**P0:** environment joblib kompatibel dan smoke test ke-14 seri; validasi setiap vektor fitur persis. **P1:** tes konsistensi report/plot otomatis, pengujian API/UI runtime, provenance/hash. **P2:** rolling-origin dan robustness musiman, pemeriksaan near-duplicate, uji drift seri/domain yang belum dilihat. **P3:** orkestrasi input terbatas dan pilot terkontrol; tidak ada kontrol energi otomatis tanpa kajian operasional independen.

## Pertanyaan umum

**Apakah forecasting live?** Tidak, Forecast Explorer menampilkan evaluasi held-out historis. **Apakah 14/14 berarti 14 model bisa dimuat?** Tidak, itu hitungan file; loading perlu diuji terpisah. **Apakah tiga dataset digabung?** Tidak, eksperimen menjaga domain/interval. **Mengapa Peak F1?** Proksi event berbasis P90 train melengkapi MAE, bukan mengukur kondisi darurat jaringan. **Bolehkah forecast hanya dengan tanggal?** Tidak, estimator memerlukan fitur historis persis. **Apakah dataset asli disertakan?** Tidak, ambil sesuai hak dan provenance asal. **Apakah siap produksi?** Belum.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
