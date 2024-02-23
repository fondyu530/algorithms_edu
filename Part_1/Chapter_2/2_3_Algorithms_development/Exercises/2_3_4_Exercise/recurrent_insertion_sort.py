def recurrent_insertion_sort(arr, end_index):
    if len(arr) > 1:
        last_el = arr[-1]
        arr = recurrent_insertion_sort(arr[:end_index-1], end_index-1)
        arr += [last_el]
        i = len(arr) - 1
        while (i > 0) and (last_el < arr[i-1]):
            if last_el < arr[i-1]:
                arr[i] = arr[i-1]
            i -= 1
        arr[i] = last_el
    return arr


input_arr = [1, 2, 6, 3, 5, 4, 18, 13, 11, 9]
initial_arr_len = len(input_arr)
print(recurrent_insertion_sort(input_arr, len(input_arr)))
