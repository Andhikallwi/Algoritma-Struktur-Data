class Buku:
    def __init__(self, judul, pengarang, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga
    
    def tampilkan_info(self):
        print(f"Judul     : {self.judul}")
        print(f"Pengarang : {self.pengarang}")
        print(f"Harga     : Rp {self.harga:,}")
        print("-" * 30)
    
    def ubah_harga(self, harga_baru):
        self.harga = harga_baru
        print(f"Harga buku '{self.judul}' telah diperbarui menjadi Rp {self.harga:,}")
buku1 = Buku("Sikancil", "=Yuli Setiani", 75000)
buku2 = Buku("Jitu lulus CPNS", "Erick Setiawan", 95000)

# Menampilkan informasi buku
buku1.tampilkan_info()
buku2.tampilkan_info()
# Mengubah harga buku pertama
buku1.ubah_harga(80000)
buku2.ubah_harga(60000)
print("-" * 30)
buku1.tampilkan_info()
buku2.tampilkan_info()