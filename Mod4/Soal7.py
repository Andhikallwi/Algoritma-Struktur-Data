def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    indices = []
    
    # Secara berulang belah runtutan itu menjadi separuhnya
    while low <= high:
        mid = (high + low) // 2
        
        if kumpulan[mid] == target:
            indices.append(mid)
            # Mencari ke kiri
            l, r = mid - 1, mid + 1
            while l >= 0 and kumpulan[l] == target:
                indices.append(l)
                l -= 1
            # Mencari ke kanan
            while r < len(kumpulan) and kumpulan[r] == target:
                indices.append(r)
                r += 1
            return sorted(indices)  # Mengembalikan semua indeks dalam urutan
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return []  # Mengembalikan list kosong jika elemen tidak ditemukan

# Contoh penggunaan
data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
target = 6
print(f"Angka {target} ditemukan di indeks: {binSe(data, target)}")