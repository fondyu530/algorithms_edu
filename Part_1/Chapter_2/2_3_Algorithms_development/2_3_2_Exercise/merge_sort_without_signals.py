import math


def merge(arr_1, arr_2):
    res_arr = []
    arr_1_len = len(arr_1)
    arr_2_len = len(arr_2)

    i = j = 0
    while True:
        if arr_1[i] < arr_2[j]:
            res_arr.append(arr_1[i])
            i += 1
        else:
            res_arr.append(arr_2[j])
            j += 1

        if i == arr_1_len:
            res_arr += arr_2[j:]
            break
        elif j == arr_2_len:
            res_arr += arr_1[i:]
            break
    return res_arr


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len > 1:
        split_index = arr_len // 2
        arr_1 = arr[:split_index]
        arr_2 = arr[split_index:]
        arr_1 = merge_sort(arr_1)
        arr_2 = merge_sort(arr_2)
        return merge(arr_1, arr_2)
    return arr


input_arr = [3, 41, 52, 26, 38, 57, 9, 49]
print(merge_sort(input_arr))
