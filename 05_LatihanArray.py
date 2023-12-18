var_arr = [1 , 7 , 2 , 89 , 3]
left_pointer = var_arr[0]

for i in range(1 , len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)