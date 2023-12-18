# Operasi pada List, Set dan String
# len()
# Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. Khusus pada string, program akan menghitung jumlah karakternya.

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

# min() dan max()
# Selain menghitung panjang atau banyaknya elemen, Anda juga dapat mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# count()
# Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# In dan Not In
# In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list. Anda bisa menggunakan operator ini untuk memastikan suatu nilai ada dalam list bahkan dalam string. Operator in dan not in akan mengembalikan nilai boolean True atau False.

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
print(apparel, color, size)

data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# Sort
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)


kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)