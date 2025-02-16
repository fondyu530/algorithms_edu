from utils import left, right


def min_heapify_recursive(arr: list[float], i: int) -> None:
    left_ind = left(i)
    right_ind = right(i)

    if left_ind < len(arr) and arr[left_ind] < arr[i]:
        smallest_ind = left_ind
    else:
        smallest_ind = i
    if right_ind < len(arr) and arr[right_ind] < arr[smallest_ind]:
        smallest_ind = right_ind
    if smallest_ind != i:
        arr[smallest_ind], arr[i] = arr[i], arr[smallest_ind]
        min_heapify_recursive(arr, smallest_ind)


if __name__ == '__main__':
    test_arr = [16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    min_heapify_recursive(test_arr, 0)
    print(test_arr)
