import math


def merge(arr_1, arr_2):
    res_arr = []
    res_len = len(arr_1) + len(arr_2)
    arr_1.append(math.inf)
    arr_2.append(math.inf)

    i = j = 0
    for k in range(res_len):
        print(i, j)
        if arr_1[i] < arr_2[j]:
            res_arr.append(arr_1[i])
            i += 1
        else:
            res_arr.append(arr_2[j])
            j += 1
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
