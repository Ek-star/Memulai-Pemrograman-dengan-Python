# For
var_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
for i in var_list:
    print(i)

for i in range(10):
    print(i)

# Range
# range(start, stop, step)
for i in range(1 , 10 , 2):
    print(i)

# While
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 # Increment

# For Bersarang
for i in range(1 , 3):
    for j in range(1 , 3):
        print(i,j)

# Kontrol Perulangan
# Break
# Menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya

for i in range(2):
    print("Perulangan luar: ", i)
    for j in range(10):
        print("Perulangan dalam: ", j)
        if j == 1:
            break

for huruf in 'Dico ding':
    if huruf == ' ':
        break

    print('Huruf saat ini: {}'.format(huruf))

# Continue
# Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan (statement) yang berada antara contibue hingga akhir blok

for huruf in 'Dico ding':
    if huruf == ' ':
        continue

    print('Huruf saat ini: {}'.format(huruf))

# Else setelah For
# Berfungsi untuk perulangan bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan
numbers = [1 , 2 , 3  , 4 , 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
    else:
        print("Angka tidak ditemukan.")

# Else setelah While
count = 0
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3 < 3 == False).")

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

# Pass
# Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun

x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memnuhi kondisi")

# List Comprehension
# Masih terkait perlu membuat sebuah list baru berdasarkan list yang sudah ada

angka = [1 , 2 , 3 , 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
# Fungsi append() untuk menambahkan nilai baru ke dalam variabel "pangkat"

angka = [1 , 2 , 3 , 4]
pangkat = [n**2 for n in angka]
print(pangkat)