import random


def quick_with_insertion_sort(arr: list) -> None:
    quicksort(arr, 0, len(arr) - 1)
    insertion_sort(arr)


def quicksort_modified(arr: list, start: int, end: int) -> None:
    if start < end and end - start > 4:
        q = randomized_partition(arr, start, end)
        quicksort(arr, start, q-1)
        quicksort(arr, q+1, end)


def quicksort(arr: list, start: int, end: int) -> None:
    if start < end:
        q = partition(arr, start, end)
        quicksort(arr, start, q-1)
        quicksort(arr, q+1, end)


def randomized_partition(arr: list, start: int, end: int) -> int:
    rand_i = random.randint(start, end)
    arr[rand_i], arr[end] = arr[end], arr[rand_i]
    return partition(arr, start, end)


def partition(arr: list, start: int, end: int) -> int:
    i = start - 1
    j = start
    all_els_are_equal_flag = True
    while j < end:
        if arr[j] != arr[end] and all_els_are_equal_flag:
            all_els_are_equal_flag = False
        if arr[j] <= arr[end]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    if all_els_are_equal_flag:
        return int((start + end) / 2)
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1


def insertion_sort(arr: list) -> None:
    for i in range(1, len(arr)):
        j = i - 1
        pivot_value = arr[i]
        while arr[j] > pivot_value and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot_value


array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
# array = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# quicksort(array, 0, len(array) - 1)
quick_with_insertion_sort(array)
print(array)
