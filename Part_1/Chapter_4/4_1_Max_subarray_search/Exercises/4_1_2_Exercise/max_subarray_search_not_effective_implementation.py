import math


def find_maximum_subarray(arr: list):
    max_sum, low, high = -math.inf, None, None
    for i in range(len(arr)):
        tmp_sum = 0
        for j in range(i, len(arr)):
            tmp_sum += arr[j]
            if max_sum < tmp_sum:
                max_sum = tmp_sum
                low, high = i, j
    return low, high, max_sum


input_arr = [-15, 8, -6, 16, 12, -4, 5, 11, -3, 1]
left, right, max_s = find_maximum_subarray(input_arr)
print(f"Input array: {input_arr}")
print(f"Max subarray: {input_arr[left:right+1]}")
print(f"Indices: {(left, right)}")
print(f"Max sum: {max_s}")
