def build_max_heap(arr: list[float]) -> list[float]:
    for i in range(len(arr) // 2 - 1, -1, -1):
        print(i)
        max_heapify_iterative(arr, i)


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


def left(ind: int) -> int:
    return (ind + 1) * 2 - 1


def right(ind: int) -> int:
    return (ind + 1) * 2


def parent(ind: int) -> int:
    if ind <= 0:
        return -1
    return (ind - 1) // 2


if __name__ == '__main__':
    test_arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    build_max_heap(test_arr)
    print(test_arr)
