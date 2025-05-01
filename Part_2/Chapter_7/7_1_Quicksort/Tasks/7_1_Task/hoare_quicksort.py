def quicksort(arr: list, start: int, end: int) -> None:
    if start < end:
        q = hoare_partition(arr, start, end)
        quicksort(arr, start, q)
        quicksort(arr, q+1, end)


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


array = [9, 19, 13, 5, 12, 8, 7, 4, 11, 2, 6, 21]
quicksort(array, 0, len(array) - 1)
print(array)
