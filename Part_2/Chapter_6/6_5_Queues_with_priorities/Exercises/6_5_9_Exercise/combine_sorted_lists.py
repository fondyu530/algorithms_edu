import math
import random

from typing import Any
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


class MinHeap(Heap):

    def delete(self, i: int) -> None:
        self.heap_arr[i] = self.heap_arr[-1]
        del self.heap_arr[-1]
        self.length -= 1
        self._heapify(i, self.length)

    def insert(self, key: Any) -> None:
        self.heap_arr.append((math.inf, -1))
        self.decrease_key(self.length, key)
        self.length += 1

    def decrease_key(self, i: int, key: Any) -> None:
        if key > self.heap_arr[i]:
            raise Exception('New key is less than old one')
        self.heap_arr[i] = key
        parent_index = self._parent(i)
        while i > 0 and self.heap_arr[parent_index] > self.heap_arr[i]:
            self.heap_arr[parent_index], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[parent_index]
            i = parent_index
            parent_index = self._parent(i)

    @property
    def heap_minimum(self) -> Any:
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
    n_lists = 3
    n_max_elements = 5

    lists_dict = {i: sorted(random.sample(range(1, 101), random.randint(0, n_max_elements))) for i in range(n_lists)}

    lists_current_positions = {i: 0 for i in range(n_lists)}

    heap = MinHeap()
    heap.build_heap_from_array([(value[0], key) for key, value in lists_dict.items() if len(value) > 0])

    result_list = []

    while heap.length > 0:
        append_list_element = heap.heap_minimum
        append_list_value = append_list_element[0]

        heap_insert_list_key = append_list_element[1]
        heap_insert_list = lists_dict[heap_insert_list_key]
        lists_current_positions[heap_insert_list_key] += 1

        heap_insert_list_index = lists_current_positions[heap_insert_list_key]

        heap.delete(0)

        if heap_insert_list_index < len(heap_insert_list):
            heap_insert_list_element = (heap_insert_list[heap_insert_list_index], heap_insert_list_key)
            heap.insert(heap_insert_list_element)

        result_list.append(append_list_value)

    print(f'Initial lists:\n')
    for key, value in lists_dict.items():
        print(f'{key}: {value}')

    print(f'\nResult list:\n{result_list}')
