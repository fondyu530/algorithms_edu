import numpy as np


class YoungTableau:

    def __init__(self, rows_num: int, cols_num: int):
        self.rows_num = rows_num
        self.cols_num = cols_num
        self.max_elements = rows_num * cols_num
        self.young_tableau = self.__build_empty_young_tableau(rows_num, cols_num)

    def __str__(self) -> str:
        return str(self.young_tableau)

    def __getitem__(self, index: int):
        return self.young_tableau[index]

    def __contains__(self, value: float) -> bool:
        i, j = 0, self.cols_num - 1
        while True:
            if value == self.young_tableau[i, j]:
                return True

            if value > self.young_tableau[i, j]:
                i += 1
            else:
                j -= 1

            if j < 0 or i >= self.rows_num:
                return False

    @staticmethod
    def __build_empty_young_tableau(rows_num: int, cols_num: int) -> np.ndarray:
        return np.zeros((rows_num, cols_num)) + np.inf

    def insert_from_array(self, array: list) -> None:
        range_arg = len(array)
        if len(array) > self.max_elements:
            range_arg = self.max_elements
            print(f'WARNING: Array length ({len(array)}) > Max tableau size ({self.max_elements}). Insertion will be '
                  f'stopped when Index == Max tableau size')

        for i in range(range_arg):
            self.insert(array[i])

    def insert(self, value: float) -> None:
        i, j = self.rows_num - 1, self.cols_num - 1
        while True:
            i_tmp, j_tmp = i, j
            upper_value = self.young_tableau[i - 1, j] if i > 0 else - np.inf
            left_value = self.young_tableau[i, j - 1] if j > 0 else - np.inf
            largest_value = value

            if left_value > value:
                largest_value = left_value
            if upper_value > largest_value:
                largest_value = upper_value

            if largest_value == left_value:
                j -= 1
            elif largest_value == upper_value:
                i -= 1
            else:
                break

            self.young_tableau[i_tmp, j_tmp] = self.young_tableau[i, j]

        self.young_tableau[i, j] = value

    def get_sorted_elements_using_extract_min(self) -> list[float]:
        sorted_result = []
        for _ in range(self.max_elements):
            sorted_result.append(self.extract_min())
        return sorted_result

    def extract_min(self) -> float:
        extract_value = self.young_tableau[0, 0]
        value = np.inf

        i = j = 0
        while True:
            i_tmp, j_tmp = i, j
            lower_value = self.young_tableau[i + 1, j] if i < self.rows_num - 1 else np.inf
            right_value = self.young_tableau[i, j + 1] if j < self.cols_num - 1 else np.inf
            smallest_value = value

            if right_value < value:
                smallest_value = right_value
            if lower_value < smallest_value:
                smallest_value = lower_value

            if smallest_value == right_value and right_value != np.inf:
                j += 1
            elif smallest_value == lower_value and lower_value != np.inf:
                i += 1
            else:
                break

            self.young_tableau[i_tmp, j_tmp] = self.young_tableau[i, j]

        self.young_tableau[i, j] = value
        return float(extract_value)

    def extract_min_recursive(self) -> float:
        extract_value = self.young_tableau[0, 0]
        self.young_tableau[0, 0] = - np.inf
        self.increase_value(0, 0, np.inf)
        return float(extract_value)

    def increase_value(self, i: int, j: int, value: float) -> None:
        if value < self.young_tableau[i, j]:
            raise Exception('New key is less than old one')
        self.young_tableau[i, j] = value
        self._keep_young_tableau_property_on_increase(i, j)

    def _keep_young_tableau_property_on_increase(self, i: int, j: int) -> None:
        tmp_i, tmp_j = i, j

        lower_value = self.young_tableau[i + 1, j] if i < self.rows_num - 1 else np.inf
        right_value = self.young_tableau[i, j + 1] if j < self.cols_num - 1 else np.inf
        smallest_value = self.young_tableau[i, j]

        if right_value < smallest_value:
            smallest_value = right_value
        if lower_value < smallest_value:
            smallest_value = lower_value

        if smallest_value == right_value and right_value != np.inf:
            j += 1
        elif smallest_value == lower_value and lower_value != np.inf:
            i += 1
        else:
            return

        self.young_tableau[i, j], self.young_tableau[tmp_i, tmp_j] = self.young_tableau[tmp_i, tmp_j], self.young_tableau[i, j]
        self._keep_young_tableau_property_on_increase(i, j)

    def get_sorted_elements(self) -> list[float]:
        current_arrays_positions = {i: 0 for i in range(len(self.young_tableau))}
        sorted_result = []

        for _ in range(self.max_elements):
            min_value = np.inf
            min_value_array_num = 0
            for i in range(self.rows_num):
                current_array_index_position = current_arrays_positions[i]
                if current_array_index_position < self.cols_num:
                    current_value = self.young_tableau[i, current_array_index_position]
                    if current_value < min_value:
                        min_value = current_value
                        min_value_array_num = i
            sorted_result.append(float(min_value))
            current_arrays_positions[min_value_array_num] += 1
        return sorted_result


if __name__ == '__main__':
    t = YoungTableau(4, 4)
    arr = [16, 14, 12, 9, 2, 3, 4, 5, 8, 18, 19, 20, 21, 22, 23, 24]
    t.insert_from_array(arr)

    print(t, end='\n\n')

    print(t.get_sorted_elements(), end='\n\n')

    print(f'2 in t: {2 in t}')
    print(f'14 in t: {14 in t}')
    print(f'24 in t: {24 in t}\n')

    print(f'1 in t: {1 in t}')
    print(f'13 in t: {13 in t}')
    print(f'25 in t: {25 in t}')
