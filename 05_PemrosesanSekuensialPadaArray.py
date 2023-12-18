var_arr = [1 , 2 , 3 , 4 , 5]
for i in range(len(var_arr)):
    curent_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {curent_element}, next elements: {next_element}")
    