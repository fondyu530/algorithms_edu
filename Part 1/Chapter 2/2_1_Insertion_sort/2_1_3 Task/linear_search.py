def linear_search(array, value) -> int:
    array_size = len(array)
    for i in range(array_size):
        if array[i] == value:
            return i


input_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
input_value = 10

value_index = linear_search(input_arr, input_value)
print(f"Found value index: {value_index}")
