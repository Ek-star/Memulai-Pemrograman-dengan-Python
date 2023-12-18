# One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris
# One-liner adalah salah satu keunggulan dalam Python yang susah untuk diimplememtasikan bagi beberapa bahasa pemrograman lainnya
# Tujuan dari One-liner ini adalah membuat satu baris kode yang singkat dan jelas

# Tanpa menggunakan One-liner
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x = ", x)
print("y = ", y)

# Menggunakan One-liner
x = 1
y = 2

x , y = y , x
print("Setelah pertukaran: ")
print("x = ", x)
print("y = ", y)
