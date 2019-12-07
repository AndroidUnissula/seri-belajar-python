#list = array

data1 = [1, 3, 5, 7, 34, 65, 76]

#mengakses list
subdata1 = data1[4]
subdata2 = data1[-3]

#memotong list
subdata3 = data1[0:4]
subdata4 = data1[2:4]
subdata5 = data1[-4:]

data2 = [100, 200, 300, 400, 500, 600, 700, 800]

#menambah list
data3 = data1 + data2

#merubah konten dari list
print(data1)
data1[4]=87
print(data1)

print(100*'=')
#mengkopi list ke variable baru
a = data1[:]

#merubah condet list dengan menggunakan metode slicing
data1[3:5] = [11,12]

#list dalam list
x = [data1,data2]

#mengakses list dalam multidimensional list
y=x[0][3]

# methods untuk list
data1.append(30) #menambahkan data list
panjang_list = len(data1)
print(panjang_list)

