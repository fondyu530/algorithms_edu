def hoare_partition(arr: list, start: int, end: int) -> int:
    pivot_value = arr[start]
    i = start - 1
    j = end + 1

    while True:
        j -= 1
        while arr[j] > pivot_value:
            j -= 1

        i += 1
        while arr[i] < pivot_value:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j


array = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
# array = [2, 1, 3, 4, 5, 6, 7, 8, 9, 21]
q = hoare_partition(array, 0, len(array) - 1)
print(array)
print(q)
