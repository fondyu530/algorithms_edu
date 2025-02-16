class Heap:

    def __init__(self):
        self.heap_arr = []
        self.length = 0

    def heapsort(self) -> None:
        heap_size = self.length
        for i in range(self.length - 1):
            self.heap_arr[0], self.heap_arr[heap_size - 1] = self.heap_arr[heap_size - 1], self.heap_arr[0]
            heap_size -= 1
            self.__max_heapify_iterative(0, heap_size)

    def build_max_heap_from_array(self, arr: list[float]) -> None:
        self.heap_arr = arr.copy()
        self.length = len(self.heap_arr)
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.__max_heapify_iterative(i, self.length)

    def __max_heapify_iterative(self, i: int, heap_size: int) -> None:
        while True:
            left_ind = self.__left(i)
            right_ind = self.__right(i)

            if left_ind < heap_size and self.heap_arr[left_ind] > self.heap_arr[i]:
                largest_ind = left_ind
            else:
                largest_ind = i
            if right_ind < heap_size and self.heap_arr[right_ind] > self.heap_arr[largest_ind]:
                largest_ind = right_ind

            if largest_ind == i:
                break
            else:
                self.heap_arr[largest_ind], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[largest_ind]
                i = largest_ind

    @staticmethod
    def __left(ind: int) -> int:
        return (ind + 1) * 2 - 1

    @staticmethod
    def __right(ind: int) -> int:
        return (ind + 1) * 2

    @staticmethod
    def __parent(ind: int) -> int:
        if ind <= 0:
            return -1
        return (ind - 1) // 2


if __name__ == '__main__':
    test_arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    heap = Heap()
    heap.build_max_heap_from_array(test_arr)
    heap.heapsort()
    print(heap.heap_arr)
