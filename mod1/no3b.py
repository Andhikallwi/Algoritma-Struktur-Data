k =(input("Masukkan huruf : "))
hv = ["a","i","u","e","o","A","I","U","E","O"]
hitung = 0
for i in k :
    if i in hv:
        hitung+=1
jml = len(k)
print ("(", jml, ",", jml-hitung, ")")