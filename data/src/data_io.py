def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada antara 0 sampai 100."""
    try:
        val = float(nilai)
        if 0 <= val <= 100:
            return True
    except ValueError:
        pass
    return False

def baca_data(nama_file):
    """Membaca siswa dari file contoh_data.txt."""
    data_siswa = []
    pesan_error = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue
                
                # Perbaikan typo dari 'splot' menjadi 'split'
                bagian = baris.split(",")
                if len(bagian) != 2:
                    pesan_error.append(f"Baris {nomor_baris} tidak valid")
                    continue
                
                nama = bagian[0].strip()
                nilai_str = bagian[1].strip()
                
                if not validasi_nilai(nilai_str):
                    pesan_error.append(f"Data pada baris {nomor_baris} tidak valid")
                    continue
                
                data_siswa.append({
                    "nama": nama,
                    "nilai": float(nilai_str)
                })
    except FileNotFoundError:
        pesan_error.append(f"File {nama_file} tidak ditemukan.")
    except OSError as e:
        pesan_error.append(f"Terjadi kesalahan saat membaca file: {e}")

    return data_siswa, pesan_error