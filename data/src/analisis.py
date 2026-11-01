def analisis_nilai(data_siswa, kkm):
    """Menganalisis data siswa untuk menentukan status lulus dan rata-rata."""
    total_nilai = 0
    jumlah_siswa = len(data_siswa)
    
    siswa_lulus = []
    siswa_remidi = []

    for siswa in data_siswa:
        total_nilai += siswa["nilai"]
        if siswa["nilai"] >= kkm:
            siswa["status"] = "Lulus"
            siswa_lulus.append(siswa)
        else:
            siswa["status"] = "Remidi"
            siswa_remidi.append(siswa)

    rata_rata = total_nilai / jumlah_siswa if jumlah_siswa > 0 else 0

    hasil = {
        "jumlah_siswa": jumlah_siswa,
        "rata_rata": rata_rata,
        "siswa_lulus": siswa_lulus,
        "siswa_remidi": siswa_remidi
    }
    return hasil

def tampilkan_laporan(hasil):
    """Menampilkan hasil analisis nilai ke terminal."""
    print("\n" + "=" * 48)
    print("                 LAPORAN HASIL ANALISIS")
    print("=" * 48)
    print(f"Total Siswa Valid : {hasil['jumlah_siswa']}")
    print(f"Rata-rata Kelas   : {hasil['rata_rata']:.2f}")
    print(f"Jumlah Lulus      : {len(hasil['siswa_lulus'])}")
    print(f"Jumlah Remidi     : {len(hasil['siswa_remidi'])}")
    print("-" * 48)
    
    print("\nDaftar Status Siswa:")
    for siswa in hasil['siswa_lulus'] + hasil['siswa_remidi']:
        print(f"- {siswa['nama']} (Nilai: {siswa['nilai']}) -> {siswa['status']}")

def simpan_laporan(hasil, file_output):
    """Menyimpan hasil laporan ke dalam file teks di folder output."""
    # Pastikan direktori output ada
    file_output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_output, "w", encoding="utf-8") as f:
        f.write("=" * 48 + "\n")
        f.write("                 LAPORAN HASIL ANALISIS\n")
        f.write("=" * 48 + "\n")
        f.write(f"Total Siswa Valid : {hasil['jumlah_siswa']}\n")
        f.write(f"Rata-rata Kelas   : {hasil['rata_rata']:.2f}\n")
        f.write(f"Jumlah Lulus      : {len(hasil['siswa_lulus'])}\n")
        f.write(f"Jumlah Remidi     : {len(hasil['siswa_remidi'])}\n")
        f.write("-" * 48 + "\n\n")
        f.write("Daftar Status Siswa:\n")
        for siswa in hasil['siswa_lulus'] + hasil['siswa_remidi']:
            f.write(f"- {siswa['nama']} (Nilai: {siswa['nilai']}) -> {siswa['status']}\n")