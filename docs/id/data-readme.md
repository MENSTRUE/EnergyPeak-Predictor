# Data — Dokumentasi Bahasa Indonesia

## Tujuan
**Primer — UCI Steel Industry Energy Consumption**: satu fasilitas industri; target `Usage_kWh`, interval 15 menit. **Sekunder — UCI ElectricityLoadDiagrams20112014**: sumber menyediakan 370 seri pelanggan; notebook default menguji 12 seri `MT_###` terpilih secara terpisah pada interval 15 menit, bukan seluruh populasi. **Pendukung — UCI Appliances Energy Prediction**: domain rumah tangga, target `Appliances`, interval 10 menit. Bundel input pada run Kaggle tercatat di `/kaggle/input/datasets/loliwibu/energypeak-predictor-dataset`. Sumber, nama berkas, interval, dan peran direkam di `reports/evaluation/source_provenance.csv`, `input_inventory.csv`. Hak penggunaan data UCI harus diperiksa per sumber; MIT pada kode tidak mengubah lisensi datanya.

## Batasan
Didukung: evaluasi retrospektif satu langkah per seri, metrik Kaggle tersimpan, pemilihan champion berbasis MAE validasi, serta indikator puncak turunan dari ambang. Tidak didukung: sensor IoT real-time, dispatch day-ahead, penghematan tarif/biaya, jaminan puncak, forecast hanya dari timestamp, aktuasi jaringan, atau generalisasi eksternal terverifikasi. Keberadaan file model tidak boleh disamakan dengan keberhasilan memuat maupun kesiapan inferensi.

## Catatan teknis
Periksa parsing/urutan timestamp, duplikasi, interval hilang, outlier, unit, cakupan seri, dan riwayat minimum yang bisa dipakai. `research_gate.json` merekam PASS_REPRODUCIBILITY serta penanda split kronologis, ambang dari train, seleksi validasi, dan pemisahan sumber. Ini gerbang otomatis notebook, bukan verifikasi independen eksternal. Fitur masa lalu wajib direkonstruksi saat inferensi; jangan memasukkan target saat ini atau variabel eksogen masa depan. Timestamp berdekatan tetap berkorelasi meski tidak ada duplikat identik.

## Pengujian
Backend: `cd backend`, aktifkan venv Python, `python -m pytest -q`, `python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`; periksa `/docs` dan `/api/v1/health`. Frontend: `cd frontend`, `npm install`, `npm run build`, `npm run dev`; buka `http://127.0.0.1:5173`. Uji integrasi manual: semua seri, pagination forecast dan empty state, schema model dan input 21 fitur yang sah, research gate, dan penanganan error. Screenshot membuktikan tampilan aplikasi lokal, bukan bukti seluruh rute/model lulus.

[README utama](../../README.md)
