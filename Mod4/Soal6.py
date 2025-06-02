def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    
    # Secara berulang belah runtutan itu menjadi separuhnya
    while low <= high:
        mid = (high + low) // 2
        
        if kumpulan[mid] == target:
            return mid  # Mengembalikan indeks lokasi elemen yang ditemukan
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False  # Mengembalikan False jika elemen tidak ditemukan

# Contoh penggunaan
data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
target = 6
print(f"Angka {target} ditemukan di indeks: {binSe(data, target)}")
