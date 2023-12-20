# Deklarasi sekaligus inisialisasi nilai matriks
matriks = [[1 , 0 , 1 , 0 , 1],
           [0 , 1 , 0 , 1, 0],
           [1 , 0 , 1 , 0 , 1]]

print (matriks)

# Deklarasi dengan nilai default
matriks = [[0 for j in range(4)] for i in range(3)]

print (matriks)

# Akses Elemen Matriks
var_mat = [[1 , 2 , 3 , 4 , 5],
           [6 , 7 , 8 , 9 , 10],
           [11 , 12 , 13 , 14 , 15],
           [16 , 17 , 18 , 19 , 20],
           [21 , 22 , 23 , 24 , 25]]

print(var_mat[2][1])