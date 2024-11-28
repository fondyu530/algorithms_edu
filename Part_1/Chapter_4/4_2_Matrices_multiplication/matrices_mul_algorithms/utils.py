from typing import Optional


def print_matrix(m: list[list[float]]) -> None:
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end='\t')
        print()
    print()


def initialize_empty_mat_mul_product(a: list[list[float]], b: list[list[float]]) -> list[list[int]]:
    a_cols_num, b_rows_num = len(a[0]), len(b)

    if a_cols_num != b_rows_num:
        raise Exception(f'Invalid matrices given! Matrix 1 cols ({a_cols_num}) != Matrix 2 row ({b_rows_num})')

    c_rows_num, c_cols_cum = len(a), len(b[0])
    empty_c = []

    for i in range(c_rows_num):
        empty_c.append([])
        for j in range(c_cols_cum):
            empty_c[i].append(0)
    return empty_c


def get_product_of_matrix_symmetric_2d_partition(
        m: list[list[float]]
) -> (list[list[float]], list[list[float]], list[list[float]], list[list[float]]):
    size = len(m) // 2
    m11 = [[m[i][j] for j in range(size)] for i in range(size)]
    m12 = [[m[i][j] for j in range(size, size * 2)] for i in range(size)]
    m21 = [[m[i][j] for j in range(size)] for i in range(size, size * 2)]
    m22 = [[m[i][j] for j in range(size, size * 2)] for i in range(size, size * 2)]
    return m11, m12, m21, m22


def sum_matrices(matrices: list[list[list[float]]], multipliers: Optional[list[float]] = None) -> list[list[float]]:
    matrices_dims = list(map(lambda x: get_matrix_dims(x), matrices))
    if len(set(matrices_dims)) > 1:
        raise Exception(
            f'Invalid matrices dimensions! All matrices should have equal dimensions. Given: {matrices_dims}'
        )
    rows_num, cols_num = matrices_dims[0][0], matrices_dims[0][1]
    res_matrix = [[0 for _ in range(cols_num)] for _ in range(rows_num)]
    multipliers = multipliers or [1 for _ in matrices]

    for matrix, multiplier in zip(matrices, multipliers):
        for i in range(rows_num):
            for j in range(cols_num):
                res_matrix[i][j] += matrix[i][j] * multiplier
    return res_matrix


def pad_matrix_with_zeros_to_square(m: list[list[float]]) -> list[list[float]]:
    rows_num, cols_num = get_matrix_dims(m)
    if not matrix_is_square_2n(rows_num, cols_num):
        square_m = []
        nearest_2n_rows_num, nearest_2n_cols_num = find_nearest_2n(rows_num), find_nearest_2n(cols_num)
        res_dimension = max(nearest_2n_rows_num, nearest_2n_cols_num)
        for i in range(res_dimension):
            square_m.append([])
            for j in range(res_dimension):
                append_value = m[i][j] if i < rows_num and j < cols_num else 0
                square_m[i].append(append_value)
        return square_m
    return m


def get_matrix_dims(m: list[list[float]]) -> (int, int):
    rows_num, cols_num = len(m), len(m[0])
    return rows_num, cols_num


def matrix_is_square_2n(rows_num: int, cols_num: int) -> bool:
    return num_is_2n(rows_num) and num_is_2n(cols_num)


def num_is_2n(num: int) -> bool:
    return not num & num - 1


def find_nearest_2n(num: int) -> int:
    num = num - 1
    while num & num - 1:
        num = num & num - 1
    return num << 1
