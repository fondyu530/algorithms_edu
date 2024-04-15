import math


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
        if arr[low] < 0:
            return low, high, 0
        return low, high, arr[low]
    elif high < 0:
        return -1, -1, -math.inf
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray_search(arr, low, mid)
    right_low, right_high, right_sum = max_subarray_search(arr, mid+1, high)
    cross_low, cross_high, cross_sum = max_cross_subarray_search(arr, low, high)
    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return left_low, left_high, left_sum
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return left_low, left_high, left_sum
    return cross_low, cross_high, cross_sum


input_arr = [-3, -2, -1]
left, right, max_s = max_subarray_search(arr=input_arr, low=0, high=len(input_arr)-1)
print(f"Input array: {input_arr}")
print(f"Max subarray: {input_arr[left:right+1] if left != right else []}")
print(f"Indices: {(left, right)}")
print(f"Max sum: {max_s}")
