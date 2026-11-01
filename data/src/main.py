from pathlib import Path
from data_io import baca_data
from analisis import analisis_nilai, tampilkan_laporan, simpan_laporan

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_DATA = Path(__file__).resolve().parent / "contoh_data.txt"
FILE_OUTPUT = BASE_DIR / "output" / "laporan_nilai.txt"
KKM = 75

def main():
    print("=" * 48)
    print("        PROGRAM ANALISIS NILAI MATEMATIKA")
    print("=" * 48)

    try:
        data_siswa, pesan_error = baca_data(FILE_DATA)
    except FileNotFoundError:
        print(f"Error: File data tidak ditemukan di {FILE_DATA}")
        return
    except OSError as error:
        print(f"Error saat membaca file: {error}")
        return

    if pesan_error:
        print("\nCatatan Data:")
        for pesan in pesan_error:
            print("-", pesan)

    if not data_siswa:
        print("\nTidak ada data siswa valid.")
        return

    # Proses analisis nilai
    hasil = analisis_nilai(data_siswa, KKM)
    
    # Tampilkan laporan di terminal
    tampilkan_laporan(hasil)

    # Simpan laporan ke folder output
    try:
        simpan_laporan(hasil, FILE_OUTPUT)
        print("\nLaporan berhasil disimpan ke folder output.")
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")

if __name__ == "__main__":
    main()