# list sebagai iterable
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:
    print(g," | panjang karakternya adalah : [",len(g),"]")


print(100*".")
# string sebagai iterable
bakwan = 'bakwan'

for i in bakwan:
    print(i)

print(100*".")
#for di dalam for
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan, buah, sayur]

for subdb in daftar_belanja:
    print(subdb)
