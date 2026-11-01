def format_rupiah(angka):
    """Fungsi utilitas opsional untuk pemformatan angka/teks jika diperlukan."""
    return f"{angka:,.2f}"

def cari_siswa_berdasarkan_nama(data_siswa, keyword):
    """Mencari siswa berdasarkan nama dalam daftar siswa."""
    hasil_pencarian = [
        siswa for siswa in data_siswa 
        if keyword.lower() in siswa["nama"].lower()
    ]
    return hasil_pencarian