from typing import Union


def print_matrix(m: list[list[Union[int, float]]]) -> None:
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


def multiply_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[Union[float, int]]]:
    c = initialize_empty_mat_mul_product(a, b)

    for i in range(len(c)):
        for j in range(len(c[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c


if __name__ == '__main__':
    A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]

    B = [
        [5, 5, 5, 5],
        [4, 4, 4, 4],
        [3, 3, 3, 3],
        [2, 2, 2, 2],
        [1, 1, 1, 1]
    ]

    C = multiply_matrices(A, B)
    print_matrix(C)
