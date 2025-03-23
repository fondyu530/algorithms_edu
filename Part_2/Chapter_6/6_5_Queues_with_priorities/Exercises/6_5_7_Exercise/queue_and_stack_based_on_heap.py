import math
from abc import ABC, abstractmethod


class Heap(ABC):

    def __init__(self):
        self.heap_arr = []
        self.length = 0

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


class Stack(Heap):

    def __init__(self):
        super().__init__()
        self.current_priority = 0

    def push(self, key) -> None:
        self.heap_arr.append((-math.inf, key))
        self._max_heap_insert(self.length, key)
        self.length += 1
        self.current_priority += 1

    def pop(self) -> float:
        return_value = self.heap_arr[0][1]
        self.heap_arr[0] = self.heap_arr[-1]
        self.length -= 1
        self._heapify(0, self.length)
        del self.heap_arr[-1]
        return return_value

    def _max_heap_insert(self, i: int, key: float) -> None:
        if self.current_priority < self.heap_arr[i][0]:
            raise Exception('New priority is less than old one')
        parent_index = self._parent(i)
        while i > 0 and self.heap_arr[parent_index][0] < self.current_priority:
            self.heap_arr[i] = self.heap_arr[parent_index]
            i = parent_index
            parent_index = self._parent(i)
        self.heap_arr[i] = (self.current_priority, key)

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


class Queue(Stack):

    def push(self, key) -> None:
        self.heap_arr.append((-math.inf, key))
        self._max_heap_insert(self.length, key)
        self.length += 1
        self.current_priority -= 1


if __name__ == '__main__':
    data_structure = Stack()

    for el in [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]:
        data_structure.push(el)

    print(data_structure.heap_arr)

    for _ in range(4):
        print(data_structure.pop())

    data_structure.push(20)
    print(data_structure.heap_arr)

    for _ in range(5):
        print(data_structure.pop())
