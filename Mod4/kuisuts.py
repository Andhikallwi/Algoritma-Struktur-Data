print("Soal No 1")
class Buku:# Kelas Buku untuk merepresentasikan data buku
    def __init__(self, judul, pengarang, harga):# Inisialisasi atribut judul, pengarang, dan harga
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga
    
    def tampilkan_info(self):# Menampilkan informasi buku
        print(f"Judul     : {self.judul}")
        print(f"Pengarang : {self.pengarang}")
        print(f"Harga     : Rp {self.harga:,}")
        print("-" * 30)
    
    def ubah_harga(self, harga_baru):# Mengubah harga buku dan mencetak pesan konfirmasi
        self.harga = harga_baru
        print(f"Harga buku '{self.judul}' telah diperbarui menjadi Rp {self.harga:,}")

buku1 = Buku("Jalan ke Rumah", "Amanda Waller", 85000)# Membuat objek buku dengan judul, pengarang, dan harga tertentu
buku2 = Buku("DI Ambang Karam", "Setiawan Budi", 115000)

buku1.tampilkan_info()# Menampilkan informasi buku
buku2.tampilkan_info()

buku1.ubah_harga(60000)# Mengubah harga buku pertama dan kedua
buku2.ubah_harga(1200000)
print("=" * 30)

buku1.tampilkan_info()# Menampilkan informasi buku setelah harga diubah
buku2.tampilkan_info()

print('\n' + "Soal No 2: Sistem pencatatan data produk di toko elektronik\n")

# Kelas Produk untuk merepresentasikan data produk
class Produk:
    def __init__(self, kode, nama, harga):# Inisialisasi atribut kode, nama, dan harga
        self.kode = kode
        self.nama = nama
        self.harga = harga 
    def __repr__(self):# Mengembalikan representasi string dari objek produk
        return f"{self.kode}: {self.nama} - Rp{self.harga}"

# Membuat daftar produk dengan kode, nama, dan harga tertentu
produk_list = [
    Produk("P001", "Laptop", 8500000),    # Produk 1: Laptop
    Produk("P002", "Smartphone", 5000000), # Produk 2: Smartphone
    Produk("P003", "Tablet", 3500000),    # Produk 3: Tablet
    Produk("P004", "Smartwatch", 2000000),# Produk 4: Smartwatch
    Produk("P005", "Monitor", 3000000)    # Produk 5: Monitor
]

def insertion_sort(arr): # Fungsi untuk mengurutkan daftar produk berdasarkan harga menggunakan Insertion Sort
    n = len(arr)  # Panjang array
    for i in range(1, n):  # Iterasi mulai dari elemen kedua
        item = arr[i]  # Elemen yang akan disisipkan
        j = i - 1
        # Memindahkan elemen yang lebih besar ke posisi berikutnya
        while j >= 0 and item.harga < arr[j].harga:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item  # Menempatkan elemen pada posisi yang sesuai

# Mengurutkan daftar produk
insertion_sort(produk_list)

# Menampilkan daftar produk setelah diurutkan
print("\nDaftar Produk Setelah Sorting (Termurah ke Termahal):")
for produk in produk_list:
    print(produk)  # Menampilkan setiap produk dalam daftar

def cari_produk(kode, daftar_produk):# Fungsi untuk mencari produk berdasarkan kode menggunakan Linear Search
    for produk in daftar_produk:  # Iterasi melalui daftar produk
        if produk.kode == kode:# Jika kode cocok, kembalikan produk
            return produk
    return None# Jika tidak ditemukan, kembalikan None

kode_cari = "P003"# Mencari produk dengan kode tertentu
hasil_pencarian = cari_produk(kode_cari, produk_list)

print("\nHasil Pencarian Produk:")# Menampilkan hasil pencarian produk
if hasil_pencarian:
    print(hasil_pencarian)  # Jika ditemukan, tampilkan produk
else:
    print("Produk tidak ditemukan.")  # Jika tidak ditemukan, tampilkan pesan