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

    c_rows_num = len(a)
    c_cols_cum = len(b[0])

    empty_c = []

    for i in range(c_rows_num):
        empty_c.append([])
        for j in range(c_cols_cum):
            empty_c[i].append(0)

    return empty_c


def pad_matrix_with_zeros(m: list[list[float]]) -> list[list[float]]:
    rows_num, cols_num = len(m), len(m[0])
    if matrix_is_square_2n(rows_num, cols_num):
        return m

    res_m = []
    nearest_2n_rows_num, nearest_2n_cols_num = find_nearest_2n(rows_num), find_nearest_2n(cols_num)
    res_dimension = max(nearest_2n_rows_num, nearest_2n_cols_num)
    for i in range(res_dimension):
        res_m.append([])
        for j in range(res_dimension):
            append_value = m[i][j] if i < rows_num and j < cols_num else 0
            res_m[i].append(append_value)
    return res_m


def matrix_is_square_2n(rows_num: int, cols_num: int) -> bool:
    return num_is_2n(rows_num) and num_is_2n(cols_num)


def num_is_2n(num: int) -> bool:
    return not num & num - 1


def find_nearest_2n(num: int) -> int:
    num = num - 1
    while num & num - 1:
        num = num & num - 1
    return num << 1
