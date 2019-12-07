number = 25

for i in range(0, 40):
    print(i)
    if i is number:
        print('angka ditemukan', i)
        break
else:
    print('angka tidak di temukan')


#break akan keluar dari proses looping
#else pada for di gunakan untuk mengecek apakan looping di lakukan sampai selesai atau tidak
