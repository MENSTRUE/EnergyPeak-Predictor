# Dataset — EnergyPeak Predictor

Dokumen ini memperluas bagian-bagian sumber kebenaran README utama. Semua angka dan keterbatasan mengacu pada keluaran repositori yang tersimpan.

## Inventaris dataset dan asal sumber

**Primer — UCI Steel Industry Energy Consumption**: satu fasilitas industri; target `Usage_kWh`, interval 15 menit. **Sekunder — UCI ElectricityLoadDiagrams20112014**: sumber menyediakan 370 seri pelanggan; notebook default menguji 12 seri `MT_###` terpilih secara terpisah pada interval 15 menit, bukan seluruh populasi. **Pendukung — UCI Appliances Energy Prediction**: domain rumah tangga, target `Appliances`, interval 10 menit. Bundel input pada run Kaggle tercatat di `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset`. Sumber, nama berkas, interval, dan peran direkam di `reports/evaluation/source_provenance.csv`, `input_inventory.csv`. Hak penggunaan data UCI harus diperiksa per sumber; MIT pada kode tidak mengubah lisensi datanya.

## Audit data dan kontrol kebocoran

Periksa parsing/urutan timestamp, duplikasi, interval hilang, outlier, unit, cakupan seri, dan riwayat minimum yang bisa dipakai. `research_gate.json` merekam PASS_REPRODUCIBILITY serta penanda split kronologis, ambang dari train, seleksi validasi, dan pemisahan sumber. Ini gerbang otomatis notebook, bukan verifikasi independen eksternal. Fitur masa lalu wajib direkonstruksi saat inferensi; jangan memasukkan target saat ini atau variabel eksogen masa depan. Timestamp berdekatan tetap berkorelasi meski tidak ada duplikat identik.

## Pembagian kronologis dan rekayasa fitur

Setiap seri dibagi 60% train / 20% validasi / 20% test yang tidak disentuh, berdasarkan waktu tanpa shuffle. Seed: 42. Lag: `1,2,3,4,8,12,24,48,96`; rolling window: `4,12,48,96`; vektor kandidat memuat 21 fitur. Makna lag 96 tergantung interval: 24 jam pada data 15 menit, tetapi 16 jam pada data 10 menit. Pastikan rolling di-shift dan hanya memakai nilai sebelumnya, dan fitur kalender tersedia pada waktu prediksi.

## Path bukti

- `reports/evaluation/`
- `reports/forecasts/`
- `reports/experiments/`
- `reports/audit/`
- `notebooks/energypeak-predictor.ipynb`
