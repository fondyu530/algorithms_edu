def tail_recursive_quicksort(arr: list, start: int, end: int) -> None:
    while start < end:
        q = partition(arr, start, end)
        tail_recursive_quicksort(arr, start, q - 1)
        start = q + 1


def tail_recursive_quicksort_modified(arr: list, start: int, end: int) -> None:
    while start < end:
        q = partition(arr, start, end)
        if q < (end + start) // 2:
            tail_recursive_quicksort_modified(arr, start, q - 1)
            start = q + 1
        else:
            tail_recursive_quicksort_modified(arr, q + 1, end)
            end = q - 1


def partition(arr: list, start: int, end: int) -> int:
    i = start - 1
    j = start
    while j < end:
        if arr[j] <= arr[end]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    # array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    # array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    tail_recursive_quicksort_modified(array, 0, len(array) - 1)
    print(array)
