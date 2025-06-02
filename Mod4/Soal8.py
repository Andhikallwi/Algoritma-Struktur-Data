import random

def tebak_angka():
    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
    
    angka_rahasia = random.randint(1, 100)
    maksimal_tebakan = 10
    tebakan_ke = 1
    
    while tebakan_ke <= maksimal_tebakan:
        try:
            tebakan = int(input(f"Masukkan tebakan ke-{tebakan_ke}:> "))
            if tebakan < angka_rahasia:
                print("Itu terlalu kecil. Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Itu terlalu besar. Coba lagi.")
            else:
                print("Ya. Anda benar!")
                return
            tebakan_ke += 1
        except ValueError:
            print("Harap masukkan angka yang valid!")
    
    print(f"Sayang sekali, Anda sudah mencoba {maksimal_tebakan} kali. Angka yang benar adalah {angka_rahasia}.")

# Jalankan permainan
tebak_angka()
