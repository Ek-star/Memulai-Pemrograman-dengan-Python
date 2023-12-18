var_list = [1 , 2 , 3]
for elemen in var_list:
    print(id(elemen))

var_arr = [9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0]
print(var_arr)

var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

# Mengakses Elemen Array
var_arr = [9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0]
print(var_arr[0])
