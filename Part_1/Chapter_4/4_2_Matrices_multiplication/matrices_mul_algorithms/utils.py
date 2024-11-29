import numpy as np


def print_matrix(m: np.array) -> None:
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end='\t')
        print()
    print()


def initialize_empty_mat_mul_product(a: np.array, b: np.array) -> np.array:
    a_cols_num, b_rows_num = len(a[0]), len(b)
    if a_cols_num != b_rows_num:
        raise Exception(f'Invalid matrices given! Matrix 1 cols ({a_cols_num}) != Matrix 2 row ({b_rows_num})')
    return np.zeros((len(a), len(b[0])))


def get_product_of_matrix_symmetric_2d_partition(m: np.array) -> (np.array, np.array, np.array, np.array):
    size = len(m) // 2
    m11 = m[:size, :size]
    m12 = m[:size, size:]
    m21 = m[size:, :size]
    m22 = m[size:, size:]
    return m11, m12, m21, m22


def pad_matrix_with_zeros_to_square(m: np.array) -> np.array:
    rows_num, cols_num = m.shape
    if not matrix_is_square_2n(rows_num, cols_num):
        nearest_2n_rows_num, nearest_2n_cols_num = find_nearest_2n(rows_num), find_nearest_2n(cols_num)
        res_dimension = max(nearest_2n_rows_num, nearest_2n_cols_num)
        square_m = np.pad(m, pad_width=((0, res_dimension - rows_num), (0, res_dimension - cols_num)), mode='constant')
        return square_m
    return m


def matrix_is_square_2n(rows_num: int, cols_num: int) -> bool:
    return num_is_2n(rows_num) and num_is_2n(cols_num)


def num_is_2n(num: int) -> bool:
    return not num & num - 1


def find_nearest_2n(num: int) -> int:
    num = num - 1
    while num & num - 1:
        num = num & num - 1
    return num << 1
