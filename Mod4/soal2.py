def cari_lokasi_mahasiswa(mahasiswa, target):
    indeks = [i for i, m in enumerate(mahasiswa) if m == target]
    return indeks  # Mengembalikan daftar indeks atau list kosong jika tidak ditemukan

def uang_saku_terkecil(mahasiswa, uang_saku):
    min_uang = min(uang_saku)  # Menemukan nilai terkecil
    indeks_min = [i for i, u in enumerate(uang_saku) if u == min_uang]  # Menemukan indeks yang sesuai
    nama_mahasiswa = [mahasiswa[i] for i in indeks_min]  # Mendapatkan nama mahasiswa dengan uang saku terkecil
    return indeks_min, nama_mahasiswa, min_uang

# Contoh penggunaan
daftar_mahasiswa = ["Jakarta", "Bandung", "Klaten", "Surabaya", "Klaten", "Medan", "Klaten", "Yogyakarta"]
uang_saku = [500000, 450000, 300000, 600000, 300000, 550000, 300000, 480000]

# Mencari mahasiswa dari Klaten
indeks_klaten = cari_lokasi_mahasiswa(daftar_mahasiswa, "Klaten")
print(f"Mahasiswa dari Klaten berada di indeks: {indeks_klaten}")

# Mencari mahasiswa dengan uang saku terkecil
indeks_terkecil, nama_terkecil, jumlah_terkecil = uang_saku_terkecil(daftar_mahasiswa, uang_saku)
print(f"uang saku terkecil {jumlah_terkecil}")


