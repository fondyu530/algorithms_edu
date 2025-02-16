from utils import left, right


def max_heapify_iterative(arr: list[float], i: int) -> None:
    while True:
        left_ind = left(i)
        right_ind = right(i)

        if left_ind < len(arr) and arr[left_ind] > arr[i]:
            largest_ind = left_ind
        else:
            largest_ind = i
        if right_ind < len(arr) and arr[right_ind] > arr[largest_ind]:
            largest_ind = right_ind

        if largest_ind == i:
            break
        else:
            arr[largest_ind], arr[i] = arr[i], arr[largest_ind]
            i = largest_ind


if __name__ == '__main__':
    test_arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    max_heapify_iterative(test_arr, 1)
    print(test_arr)
