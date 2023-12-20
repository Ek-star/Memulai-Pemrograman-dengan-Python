import numpy as np

# Membuat matriks 2 x 2
var_mat = [[5 , 0],
           [1 , -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j] * 2
  
print(def_mat)

var_mat = np.array([[5 , 0],
                    [1 , -2]])

result = var_mat * 2
print(result)