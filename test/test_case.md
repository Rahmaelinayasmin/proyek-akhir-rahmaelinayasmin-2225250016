# Dokumen Pengujian (Test Case) - Proyek Akhir Analisis Nilai

## 1. Pengujian Pembacaan Data (`data_io.py`)
- **TC-01 (File Ditemukan & Valid):** Sistem membaca file `contoh_data.txt` yang berisi data nama dan nilai valid dengan pemisah koma `,`.
  - *Hasil yang diharapkan:* Seluruh data siswa berhasil dimasukkan ke dalam list tanpa error.
- **TC-02 (File Tidak Ditemukan):** Menguji penanganan ketika file teks tidak ada atau salah path.
  - *Hasil yang diharapkan:* Program menangkap `FileNotFoundError` dan mencetak pesan error dengan rapi tanpa menghentikan paksa aplikasi.

## 2. Pengujian Analisis Nilai (`analisis.py`)
- **TC-03 (Perhitungan KKM & Rata-rata):** 
  - *Input:* Daftar nilai siswa dan batas KKM = 75.
  - *Hasil yang diharapkan:* Siswa dengan nilai $\ge 75$ berstatus **Lulus**, sedangkan di bawah 75 berstatus **Remidi**. Rata-rata kelas dihitung secara akurat.

## 3. Pengujian Penyimpanan Laporan
- **TC-04 (Simpan ke Folder Output):** 
  - *Hasil yang diharapkan:* Folder `output/` terbuat secara otomatis (jika belum ada) dan file `laporan_nilai.txt` tersimpan dengan format laporan yang bersih.