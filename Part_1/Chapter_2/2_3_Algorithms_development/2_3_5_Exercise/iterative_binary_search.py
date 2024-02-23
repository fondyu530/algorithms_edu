def binary_search(arr, value):
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        middle = (left_index + right_index) // 2
        if value == arr[middle]:
            return middle
        elif value < arr[middle]:
            right_index = middle - 1
        else:
            left_index = middle + 1
    return None


input_arr = [1, 3, 5, 7, 9, 11]
print(binary_search(input_arr, 8))
