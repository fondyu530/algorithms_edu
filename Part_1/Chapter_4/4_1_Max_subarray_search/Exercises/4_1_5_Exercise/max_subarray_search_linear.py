import math


def max_subarray_search_linear(arr):
    max_sum = -math.inf
    tmp_sum = 0
    start_ind = end_ind = 0
    for i in range(len(arr)):
        tmp_sum = tmp_sum + arr[i]
        if tmp_sum < 0:
            tmp_sum = 0
            start_ind = i + 1
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            end_ind = i
    return start_ind, end_ind, max_sum


input_arr = [-15, 8, -6, 16, 12, -4, 5, 11, -3, 1]
left, right, max_s = max_subarray_search_linear(input_arr)
print(f"Input array: {input_arr}")
print(f"Max subarray: {input_arr[left:right+1]}")
print(f"Indices: {(left, right)}")
print(f"Max sum: {max_s}")
