def binary_search(arr, value, left_lim, right_lim):
    middle = (left_lim + right_lim) // 2
    if left_lim > right_lim:
        return None
    if arr[middle] == value:
        return middle
    compare_value = arr[middle]
    if value < compare_value:
        return binary_search(arr, value, left_lim, middle-1)
    if value > compare_value:
        return binary_search(arr, value, middle+1, right_lim)


input_arr = [1, 3, 5, 7, 9, 11]
left = 0
right = len(input_arr)-1

res = binary_search(input_arr, 1, left, right)
print(res)
