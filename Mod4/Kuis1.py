# Data Mahasiswa
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, nilai):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nilai = nilai

    def __repr__(self):
        return f"{self.nama}: {self.nilai}"

c0 = Mahasiswa('Ika', 75)
c1 = Mahasiswa('Budi', 80)
c2 = Mahasiswa('Ahmad', 65)
c3 = Mahasiswa('Chandra', 90)
c4 = Mahasiswa('Eka', 70)
c5 = Mahasiswa('Fandi', 85)
c6 = Mahasiswa('Deni', 95)

Daftar = [c0, c1, c2, c3, c4, c5, c6]

# Soal 1
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]  
        pos = i
        while pos > 0 and nilai.nilai > A[pos - 1].nilai:  
            A[pos] = A[pos - 1]
            pos -= 1
        A[pos] = nilai

print("Data sebelum sortir:")
for mahasiswa in Daftar:
    print(mahasiswa)

insertionSort(Daftar)

print("\nData setelah sortir (nilai tinggi ke rendah):")
for mahasiswa in Daftar:
    print(mahasiswa)

# soal 2


tinggi_atlet = [175, 180, 165, 190, 170, 185, 160]

def insertionSortDesc(A):
    n=len(A)
    for 1 in range(1, n):
        nilai = A[i]
        while pos > 0 and nilai >A [pos-1]:
        A[pos] = A[pos - 1]
    POS = pOS -1 Alposl = nilal BA = [9,2,6,4, 8,1,5]
BA = list(map(int, input("Masukkan daftar Angka: “).split()))
nilai_ujian = (75, 88,65, 90, 70, 85, 95, 60]
print ("Data sebelun di sorting: ",A)
insertionSort(A)
print ("Data setelah dilakukan sorting Ascending: ",A)
insertionSortDesc(A)
print ("Data setelah dilakukan sorting Descending:", A)