import random


def quicksort_modified_for_duplicates(arr: list, start: int, end: int) -> None:
    if start < end:
        q, t = randomized_partition_modified_for_duplicates(arr, start, end)
        quicksort_modified_for_duplicates(arr, start, q-1)
        quicksort_modified_for_duplicates(arr, t+1, end)


def randomized_partition_modified_for_duplicates(arr: list, start: int, end: int) -> int:
    rand_i = random.randint(start, end)
    arr[rand_i], arr[end] = arr[end], arr[rand_i]
    return partition_modified_for_duplicates(arr, start, end)


def partition_modified_for_duplicates(arr: list, start: int, end: int) -> (int, int):
    i = start - 1
    j = start
    k = 0
    while j < end:
        was_inside_first_condition = False
        if arr[j] < arr[end]:
            was_inside_first_condition = True
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if arr[j] == arr[end]:
            if not was_inside_first_condition:
                k += 1
            arr[i + k], arr[j] = arr[j], arr[i + k]

        j += 1
    arr[i + k + 1], arr[end] = arr[end], arr[i + k + 1]
    return i + 1, i + k + 1


# array = [8, 13, 19, 9, 9, 5, 12, 11, 6, 8, 7, 4, 11, 2, 21, 2, 6, 11, 21]
array = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
quicksort_modified_for_duplicates(array, 0, len(array) - 1)
print(array)
