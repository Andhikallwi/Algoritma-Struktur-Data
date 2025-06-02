def cari_lokasi_mahasiswa(mahasiswa, target):
    indeks = [i for i, m in enumerate(mahasiswa) if m == target]
    return indeks  # Mengembalikan daftar indeks atau list kosong jika tidak ditemukan

# Contoh penggunaan
daftar_mahasiswa = ["Jakarta", "Bandung", "Klaten", "Surabaya", "Klaten", "Medan", "Klaten", "Yogyakarta"]

# Mencari mahasiswa dari Klaten
indeks_klaten = cari_lokasi_mahasiswa(daftar_mahasiswa, "Surakarta")
print(f"Mahasiswa dari Klaten berada di indeks: {indeks_klaten}")
