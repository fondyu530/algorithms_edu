import math
from abc import ABC, abstractmethod


class Heap(ABC):

    def __init__(self):
        self.heap_arr = []
        self.length = 0

    def build_heap_from_array(self, arr: list[float]) -> None:
        self.heap_arr = arr.copy()
        self.length = len(self.heap_arr)
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify(i, self.length)

    @abstractmethod
    def _heapify(self, i: int, heap_size: int) -> None:
        pass

    @staticmethod
    def _left(ind: int) -> int:
        return (ind + 1) * 2 - 1

    @staticmethod
    def _right(ind: int) -> int:
        return (ind + 1) * 2

    @staticmethod
    def _parent(ind: int) -> int:
        if ind <= 0:
            return -1
        return (ind - 1) // 2


class MaxHeap(Heap):

    def delete(self, i: int) -> None:
        self.heap_arr[i] = self.heap_arr[-1]
        del self.heap_arr[-1]
        self.length -= 1
        self._heapify(i, self.length)

    def insert(self, key: float) -> None:
        self.heap_arr.append(-math.inf)
        self.increase_key(self.length, key)
        self.length += 1

    def increase_key(self, i: int, key: float) -> None:
        if key < self.heap_arr[i]:
            raise Exception('New key is less than old one')
        self.heap_arr[i] = key
        parent_index = self._parent(i)
        while i > 0 and self.heap_arr[parent_index] < self.heap_arr[i]:
            self.heap_arr[parent_index], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[parent_index]
            i = parent_index
            parent_index = self._parent(i)

    def increase_key_like_insertion_sort_inner_loop(self, i: int, key: float) -> None:
        if key < self.heap_arr[i]:
            raise Exception('New key is less than old one')
        parent_index = self._parent(i)
        while i > 0 and self.heap_arr[parent_index] < key:
            self.heap_arr[i] = self.heap_arr[parent_index]
            i = parent_index
            parent_index = self._parent(i)
        self.heap_arr[i] = key

    def heap_extract_max(self) -> float:
        heap_maximum = self.heap_arr[0]
        self.heap_arr[0], self.heap_arr[-1] = self.heap_arr[-1], self.heap_arr[0]
        self._heapify(0, self.length - 1)
        del self.heap_arr[-1]
        self.length -= 1
        return heap_maximum

    @property
    def heap_maximum(self) -> float:
        return self.heap_arr[0]

    def _heapify(self, i: int, heap_size: int) -> None:
        while True:
            left_ind = self._left(i)
            right_ind = self._right(i)

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


class MinHeap(Heap):

    def delete(self, i: int) -> None:
        self.heap_arr[i] = self.heap_arr[-1]
        del self.heap_arr[-1]
        self.length -= 1
        self._heapify(i, self.length)

    def insert(self, key: float) -> None:
        self.heap_arr.append(math.inf)
        self.decrease_key(self.length, key)
        self.length += 1

    def decrease_key(self, i: int, key: float) -> None:
        if key > self.heap_arr[i]:
            raise Exception('New key is less than old one')
        self.heap_arr[i] = key
        parent_index = self._parent(i)
        while i > 0 and self.heap_arr[parent_index] > self.heap_arr[i]:
            self.heap_arr[parent_index], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[parent_index]
            i = parent_index
            parent_index = self._parent(i)

    def heap_extract_min(self) -> float:
        heap_minimum = self.heap_arr[0]
        self.heap_arr[0], self.heap_arr[-1] = self.heap_arr[-1], self.heap_arr[0]
        self._heapify(0, self.length - 1)
        del self.heap_arr[-1]
        self.length -= 1
        return heap_minimum

    @property
    def heap_minimum(self) -> float:
        return self.heap_arr[0]

    def _heapify(self, i: int, heap_size: int) -> None:
        while True:
            left_ind = self._left(i)
            right_ind = self._right(i)

            if left_ind < heap_size and self.heap_arr[left_ind] < self.heap_arr[i]:
                smallest_ind = left_ind
            else:
                smallest_ind = i
            if right_ind < heap_size and self.heap_arr[right_ind] < self.heap_arr[smallest_ind]:
                smallest_ind = right_ind

            if smallest_ind == i:
                break
            else:
                self.heap_arr[smallest_ind], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[smallest_ind]
                i = smallest_ind


if __name__ == '__main__':
    test_arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    heap = MaxHeap()

    heap.build_heap_from_array(test_arr)
    print('Heap after build:')
    print(heap.heap_arr, end='\n\n')

    # heap.increase_key(7, 100)
    heap.increase_key_like_insertion_sort_inner_loop(7, 100)
    print('Heap after increase key:')
    print(heap.heap_arr, end='\n\n')

    heap.delete(1)
    print('Heap after delete:')
    print(heap.heap_arr, end='\n\n')
