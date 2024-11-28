from .general_matrices_mul import multiply_matrices
from .utils import print_matrix, pad_matrix_with_zeros_to_square, initialize_empty_mat_mul_product


def multiply_matrices_recursive_optimal(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    c_res_rows_num, c_res_cols_num = len(a), len(b[0])
    a, b = pad_matrix_with_zeros_to_square(a), pad_matrix_with_zeros_to_square(b)
    c = initialize_empty_mat_mul_product(a, b)

    def _multiply_matrices_recursive_optimal(
            row_a_ind: int,
            col_a_ind: int,
            row_b_ind: int,
            col_b_ind: int,
            size: int
    ) -> None:
        nonlocal a, b, c

        if size == 1:
            c[row_a_ind][col_b_ind] += a[row_a_ind][col_a_ind] * b[row_b_ind][col_b_ind]
        else:
            a11_sub_matrix_indices, a12_sub_matrix_indices, a21_sub_matrix_indices, a22_sub_matrix_indices = (
                get_indices_of_matrix_symmetric_2d_partition(row_a_ind, col_a_ind, size)
            )
            b11_sub_matrix_indices, b12_sub_matrix_indices, b21_sub_matrix_indices, b22_sub_matrix_indices = (
                get_indices_of_matrix_symmetric_2d_partition(row_b_ind, col_b_ind, size)
            )

            half_size = size // 2

            _multiply_matrices_recursive_optimal(*a11_sub_matrix_indices, *b11_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a12_sub_matrix_indices, *b21_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a11_sub_matrix_indices, *b12_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a12_sub_matrix_indices, *b22_sub_matrix_indices, half_size)

            _multiply_matrices_recursive_optimal(*a21_sub_matrix_indices, *b11_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a22_sub_matrix_indices, *b21_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a21_sub_matrix_indices, *b12_sub_matrix_indices, half_size)
            _multiply_matrices_recursive_optimal(*a22_sub_matrix_indices, *b22_sub_matrix_indices, half_size)

    _multiply_matrices_recursive_optimal(row_a_ind=0, col_a_ind=0, row_b_ind=0, col_b_ind=0, size=len(c))
    return [[c[i][j] for j in range(c_res_cols_num)] for i in range(c_res_rows_num)]


def get_indices_of_matrix_symmetric_2d_partition(
        row_ind: int,
        col_ind: int,
        initial_size: int
) -> ((int, int), (int, int), (int, int), (int, int)):
    half_size = initial_size // 2
    sub_matrix_11_indices = (row_ind, col_ind)
    sub_matrix_12_indices = (row_ind, col_ind + half_size)
    sub_matrix_21_indices = (row_ind + half_size, col_ind)
    sub_matrix_22_indices = (row_ind + half_size, col_ind + half_size)

    return sub_matrix_11_indices, sub_matrix_12_indices, sub_matrix_21_indices, sub_matrix_22_indices


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
        [5, 5, 5, 5, 5],
        [4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3],
        [2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1]
    ]

    C = multiply_matrices(A, B)
    print('General mul function:')
    print_matrix(C)

    C = multiply_matrices_recursive_optimal(A, B)
    print('Recursive mul function:')
    print_matrix(C)
