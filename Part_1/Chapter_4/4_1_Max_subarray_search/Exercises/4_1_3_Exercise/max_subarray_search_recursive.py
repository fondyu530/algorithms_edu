import math
import time

import pandas as pd
import plotly.express as px


def max_subarray_search_ineffective(arr: list):
    max_sum, low, high = -math.inf, None, None
    for i in range(len(arr)):
        tmp_sum = 0
        for j in range(i, len(arr)):
            tmp_sum += arr[j]
            if max_sum < tmp_sum:
                max_sum = tmp_sum
                low, high = i, j
    return low, high, max_sum


def max_cross_subarray_search(arr, low, high):
    mid = (low + high) // 2
    left_max_sum, tmp_sum, left_ind = -math.inf, 0, -1
    for i in range(mid, low-1, -1):
        tmp_sum += arr[i]
        if tmp_sum > left_max_sum:
            left_max_sum = tmp_sum
            left_ind = i

    right_max_sum, tmp_sum, right_ind = -math.inf, 0, -1
    for i in range(mid+1, high+1):
        tmp_sum += arr[i]
        if tmp_sum > right_max_sum:
            right_max_sum = tmp_sum
            right_ind = i

    return left_ind, right_ind, right_max_sum + left_max_sum


def max_subarray_search(arr, low, high):
    if low == high:
        return low, high, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray_search(arr, low, mid)
    right_low, right_high, right_sum = max_subarray_search(arr, mid+1, high)
    cross_low, cross_high, cross_sum = max_cross_subarray_search(arr, low, high)
    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return left_low, left_high, left_sum
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return left_low, left_high, left_sum
    return cross_low, cross_high, cross_sum


def max_subarray_search_modified(arr, low, high):
    if len(arr[low:high+1]) < 50:
        return max_subarray_search_ineffective(arr[low:high+1])
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray_search(arr, low, mid)
    right_low, right_high, right_sum = max_subarray_search(arr, mid+1, high)
    cross_low, cross_high, cross_sum = max_cross_subarray_search(arr, low, high)
    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return left_low, left_high, left_sum
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return left_low, left_high, left_sum
    return cross_low, cross_high, cross_sum


# base_input_arr = [-15, 8, -6, 16, 12, -4, 5, 11, -3, 1]
# base_input_arr_len = len(base_input_arr)
# time_df = pd.DataFrame()
#
# for i in range(1, 1001, 1):
#     print(base_input_arr_len + i)
#     tmp_arr = base_input_arr + [3] * i
#
#     tic = time.time()
#     res_logn = max_subarray_search(tmp_arr, 0, len(tmp_arr)-1)
#     toc = time.time()
#     logn_time = toc - tic
#
#     tic = time.time()
#     res_sq = max_subarray_search_ineffective(tmp_arr)
#     toc = time.time()
#     sq_time = toc - tic
#
#     tic = time.time()
#     res_mod = max_subarray_search_modified(tmp_arr, 0, len(tmp_arr)-1)
#     toc = time.time()
#     mod_time = toc - tic
#
#     print(res_mod == res_sq == res_logn)
#
#     logn_df = pd.DataFrame({"arr_size": [len(tmp_arr)], "time": [logn_time], "type": ["n * logn"]})
#     sq_df = pd.DataFrame({"arr_size": [len(tmp_arr)], "time": [sq_time], "type": ["n ^ 2"]})
#     mod_df = pd.DataFrame({"arr_size": [len(tmp_arr)], "time": [mod_time], "type": ["n * logn (modif)"]})
#
#     time_df = pd.concat([time_df, logn_df, sq_df, mod_df])
#
# fig = px.line(time_df, x="arr_size", y="time", color="type")
# fig.show()

input_arr = [-15, 8, -6, 16, 12, -4, 5, 11, -3, 1]
left, right, max_s = max_subarray_search(arr=input_arr, low=0, high=len(input_arr)-1)
print(f"Input array: {input_arr}")
print(f"Max subarray: {input_arr[left:right+1] if left != right else []}")
print(f"Indices: {(left, right)}")
print(f"Max sum: {max_s}")
