# Proposal Proyek Akhir: Program Analisis Nilai Matematika

## 1. Latar Belakang
Dalam kegiatan pengolahan data akademik, rekapitulasi dan analisis nilai siswa sering kali dilakukan secara manual, sehingga rentan terhadap kesalahan hitung dan membutuhkan waktu yang lebih lama. Oleh karena itu, diperlukan sebuah program otomatis berbasis Python untuk membaca data nilai, melakukan validasi, menghitung rata-rata kelas, menentukan status kelulusan berdasarkan KKM (Kriteria Ketuntasan Minimal), serta menghasilkan laporan yang terstruktur.

## 2. Tujuan Proyek
* Membangun aplikasi berbasis modular (*Modular Programming*) menggunakan Python.
* Mengotomatisasi proses pembacaan data nilai dari file teks eksternal.
* Menganalisis kelulusan siswa secara akurat berdasarkan KKM yang ditentukan.
* Menyimpan hasil rekapitulasi laporan secara otomatis ke dalam folder keluaran (*output*).

## 3. Ruang Lingkup Proyek
* **Input:** File teks (`contoh_data.txt`) yang berisi daftar nama siswa beserta nilai matematika.
* **Proses:** 
  * Validasi format data dan rentang nilai (0 - 100).
  * Perhitungan rata-rata nilai kelas.
  * Penentuan status siswa (Lulus / Remidi) berdasarkan KKM = 75.
* **Output:** Tampilan laporan di terminal serta penyimpanan file teks laporan di dalam folder `output/`.

## 4. Struktur Tim & Pembagian Tugas
* **Pengembang Utama:** Menulis kode logika utama (`main.py`, `analisis.py`, dan `data_io.py`).
* **Dokumentasi & Pengujian:** Menyusun dokumen `README.md`, `proposal.md`, serta skenario pengujian (`tests/test_case.md`).

## 5. Kesimpulan
Proyek ini diharapkan dapat mempermudah proses rekapitulasi nilai secara efisien, terstruktur, dan meminimalisir kesalahan manusia (*human error*) dalam pengolahan data akademik sederhana.