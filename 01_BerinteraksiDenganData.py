# DATA TYPING
# Deklarasi dan Inisialisasi

age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

x = 6
print(type(x))

x = "6"
print(type(x))

# Tipe Data Primitif
# Numbers -> Integer, Float, Complex
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah. Mari lihat contoh di bawah ini.

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boolean
# True , False

x = True
print(type(x))

x = False
print(type(x))

# String
x = "Dicoding"
print(type(x))

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu."""
print(multi_line)

x = "Ekalma Toto Alloy Sembiring"
print(x[0])

x = "Ekalma Toto Alloy Sembiring"
print(x[2:])

# Formatted String
name = "Ekalma Toto Alloy Sembiring"
print(f"Hello, nama saya {name}")

# %-Formatting
name = "Ekalma Toto Alloy Sembiring"
print("Nama saya %s" % (name))

# str.format()
name = "Ekalma Toto Alloy Sembiring"
print("Nama saya {}".format(name))

# Tipe Data Collection
# List -> Ordered sequence / data terurut -> []
x = [1 , 2.2 , 'Ekalma Toto Alloy Sembiring']
print(type(x))
print(x[2])
x[0] = "Indonesia"
print(x)

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

# Konsep Slicing
# sequence[start:stop:step]
# Start merupakan indeks pertama yang anda ambil
# Stop merupakan indeks terakhir yang ingin anda ambil
# Step merupakan jumlah elemen yang ingin anda lewati diantara setiap elemen slice (default = 1)

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

# Tuple -> Tidak dapat diubah (immutable)
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.
x = (1 , "Dicoding" , 1 + 3j)
print(type(x))

# Set
# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collction), dan dapat diinisialisasikan dengan kurawal "{}" dimana setiap elemennya dipisahkan dengan koma.
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

set1 = {1 , 2 , 3 , 4 , 5}
set2 = {4 , 5 , 6 , 7 , 8}
union = set1.union(set2)
print("Union:", union)

intersectin = set1.intersection(set2)
print("Intersection:", intersectin)

# Dictionary
# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut
# 1. Setiap elemen pasangan key-value dipisahkan dengan koma (,)
# 2. Key dan value dipisahkan dengan titik dua (:)
# 3. Key dan value dapat berupa tipe variabel / objek apa pun

x = { 'name' : "Ekalma Toto Alloy Sembiring" , 'age' : 20 , "isMarried": False }
print(type(x))
print(x ['name'])

# Menambah data pada dictionary
x ['Job'] = "Web Developer"

# Menghapus data pada dicitonary
x = { "name" : "Ekalma Toto Alloy Sembiring" , 'age' : 20 , 'isMarried' : False }

del x['isMarried']
print(x)

# Mengubah data pada dictionary
x = { 'name' : "Ekalma Toto Alloy Sembiring" , 'age' : 20 , "isMarried" : False }
x['name'] = 'Dicoding'
print(x)

# Konversi antara Tipe Data
# Integer ke Float
print(float(5))
# Float ke Integer
print(int(5.6))
print(int(-5.6))
# Dari-Dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
# Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
# Konversi ke Dictionary
print(dict([[1,2] , [3,4]]))