import random


def fuzzy_quicksort(arr: list, start: int, end: int) -> None:
    if start < end:
        q, t = fuzzy_randomized_partition(arr, start, end)
        fuzzy_quicksort(arr, start, q-1)
        fuzzy_quicksort(arr, t+1, end)


def fuzzy_randomized_partition(arr: list, start: int, end: int) -> int:
    rand_i = random.randint(start, end)
    arr[rand_i], arr[end] = arr[end], arr[rand_i]
    return fuzzy_partition(arr, start, end)


def fuzzy_partition(arr: list, start: int, end: int) -> (int, int):
    i = start - 1
    j = start
    k = 0
    while j < end:
        was_inside_first_condition = False
        if arr[j][0] < arr[end][0] and not is_intersection(arr[j], arr[end]):
            was_inside_first_condition = True
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if is_intersection(arr[j], arr[end]):
            if not was_inside_first_condition:
                k += 1
            arr[i + k], arr[j] = arr[j], arr[i + k]
        j += 1
    arr[i + k + 1], arr[end] = arr[end], arr[i + k + 1]
    return i + 1, i + k + 1


def is_intersection(a: (float, float), b: (float, float)) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


# array = [(23, 25), (1, 4), (5, 6), (19, 22), (7, 9), (11, 16)]
array = [(23, 25), (1, 4), (2, 6), (19, 25), (7, 9), (8, 16), (4, 6)]
# array = [(5, 6), (4, 7), (3, 8), (2, 9), (1, 10), (0, 11)]
fuzzy_quicksort(array, 0, len(array) - 1)
print(array)
