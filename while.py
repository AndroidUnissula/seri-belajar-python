#for itu kita tidak usah menambahkan increment
#while : kita perlu menambahkan nilai agar nilai bertambah
angka = 0
while angka < 5:
    print('nilai angka adalah:', angka)
    angka+=1 # atau => angka = angka + 1

print("di luar while")

print('='*100)

start = True
angka = 0

while start:
    print("di dalam while")
    if angka is 100:
        start = False
        print("oke angka 100 telah di ketemukan")
    angka +=1

