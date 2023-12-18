a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10
"""
# Mari kita bedah satu persatu kode di atas.

# Variabel a bernilai True, jika kita memberikan ekspresi "not a" yang artinya "not True", hasil yang didapat adalah False.
# Baik increment maupun decrement, keduanya adalah pola yang sama untuk menambahkan dan mengurangi suatu variabel dengan jumlah tetap.
# a += 1 memiliki tujuan yang sama dengan struktur a = a + 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi penjumlahan "1+1". Inilah alasan ia disebut dengan increment yang artinya kenaikan.
# Decrement dapat dijelaskan sebagai a -=1, memiliki tujuan yang sama dengan struktur a = a - 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi pengurangan "1-1".

print(2 + 2)
print(3 < 10)
print(True or False)

"""
Output:
4
True
True
"""