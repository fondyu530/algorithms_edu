from matrices_multiplication import multiply_matrices
from utils import print_matrix, pad_matrix_with_zeros


def multiply_matrices_recursive(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    c_res_rows_num, c_res_cols_num = len(a), len(b[0])
    a = pad_matrix_with_zeros(a)
    b = pad_matrix_with_zeros(b)

    def _multiply_matrices_recursive(
            row_a_ind: int,
            col_a_ind: int,
            row_b_ind: int,
            col_b_ind: int,
            size: int
    ) -> list[list[float]]:
        nonlocal a, b

        c = [[0 for _ in range(size)] for _ in range(size)]

        if size == 1:
            c[0][0] = a[row_a_ind][col_a_ind] * b[row_b_ind][col_b_ind]
        else:
            size //= 2
            a11_sub_matrix_indices, a12_sub_matrix_indices, a21_sub_matrix_indices, a22_sub_matrix_indices = (
                divide_matrix(row_a_ind, col_a_ind, size)
            )
            b11_sub_matrix_indices, b12_sub_matrix_indices, b21_sub_matrix_indices, b22_sub_matrix_indices = (
                divide_matrix(row_b_ind, col_b_ind, size)
            )
            c11_sub_matrix_indices, c12_sub_matrix_indices, c21_sub_matrix_indices, c22_sub_matrix_indices = (
                divide_matrix(row_ind=0, col_ind=0, divided_size=size)
            )

            sum_intermediate_matrices(
                c,
                _multiply_matrices_recursive(*a11_sub_matrix_indices, *b11_sub_matrix_indices, size),
                _multiply_matrices_recursive(*a12_sub_matrix_indices, *b21_sub_matrix_indices, size),
                *c11_sub_matrix_indices
            )

            sum_intermediate_matrices(
                c,
                _multiply_matrices_recursive(*a11_sub_matrix_indices, *b12_sub_matrix_indices, size),
                _multiply_matrices_recursive(*a12_sub_matrix_indices, *b22_sub_matrix_indices, size),
                *c12_sub_matrix_indices
            )

            sum_intermediate_matrices(
                c,
                _multiply_matrices_recursive(*a21_sub_matrix_indices, *b11_sub_matrix_indices, size),
                _multiply_matrices_recursive(*a22_sub_matrix_indices, *b21_sub_matrix_indices, size),
                *c21_sub_matrix_indices
            )

            sum_intermediate_matrices(
                c,
                _multiply_matrices_recursive(*a21_sub_matrix_indices, *b12_sub_matrix_indices, size),
                _multiply_matrices_recursive(*a22_sub_matrix_indices, *b22_sub_matrix_indices, size),
                *c22_sub_matrix_indices
            )
        return c

    c_res = _multiply_matrices_recursive(row_a_ind=0, col_a_ind=0, row_b_ind=0, col_b_ind=0, size=len(a))
    c_res = [[c_res[i][j] for j in range(c_res_cols_num)] for i in range(c_res_rows_num)]
    return c_res


def divide_matrix(
        row_ind: int,
        col_ind: int,
        divided_size: int
) -> ((int, int), (int, int), (int, int), (int, int)):
    sub_matrix_11_indices = (row_ind, col_ind)
    sub_matrix_12_indices = (row_ind, col_ind + divided_size)
    sub_matrix_21_indices = (row_ind + divided_size, col_ind)
    sub_matrix_22_indices = (row_ind + divided_size, col_ind + divided_size)

    return sub_matrix_11_indices, sub_matrix_12_indices, sub_matrix_21_indices, sub_matrix_22_indices


def sum_intermediate_matrices(
        c: list[list[float]],
        c_sub_1: list[list[float]],
        c_sub_2: list[list[float]],
        row_ind: int,
        col_ind: int
) -> None:
    for i in range(row_ind, row_ind + len(c_sub_1)):
        for j in range(col_ind, col_ind + len(c_sub_1)):
            c[i][j] = c_sub_1[i-row_ind][j-col_ind] + c_sub_2[i-row_ind][j-col_ind]


if __name__ == '__main__':
    A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
        [6, 6, 6, 6, 6],
        [7, 7, 7, 7, 7]
    ]

    B = [
        [5, 5, 5, 5],
        [4, 4, 4, 4],
        [3, 3, 3, 3],
        [2, 2, 2, 2],
        [1, 1, 1, 1]
    ]

    C = multiply_matrices(A, B)
    print('General mul function:')
    print_matrix(C)

    C = multiply_matrices_recursive(A, B)
    print('Recursive mul function:')
    print_matrix(C)
