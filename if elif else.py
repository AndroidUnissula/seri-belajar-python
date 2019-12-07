nilai = 60
if nilai == 75: #equal eksprisit
    print('nilai anda : ',nilai)

if nilai is 60: #equal
    print("nilai anda :",nilai)

if nilai is not 80: #not equal
    print('nilai anda bukan bukan 80',)

print(100*'=')

nilai = 85

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print(100*'+')
print("operator logika untuk list dan string")
print(' ')
gorengan = ["bakwan", "cireng", "bala-bala", "gehu", "combro", "pisang gorang", "pukis", "risoles"]
beli = "cireng"

if beli in gorengan:
    print('Mamang bilang,"ya, saya jual',beli, '"')

if not beli in gorengan:
    print("saya tidak jual",beli)

karakter="r"
if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada", karakter,"di",beli)