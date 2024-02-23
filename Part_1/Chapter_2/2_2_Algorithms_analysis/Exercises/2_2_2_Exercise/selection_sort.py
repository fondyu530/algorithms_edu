import math


def selection_sort(array):
    array_size = len(array)
    for i in range(array_size-1):
        min_value = math.inf
        min_value_index = 0
        for j in range(i, array_size, 1):
            if array[j] < min_value:
                min_value = array[j]
                min_value_index = j
        array[i], array[min_value_index] = array[min_value_index], array[i]


input_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
selection_sort(input_array)
print(input_array)
