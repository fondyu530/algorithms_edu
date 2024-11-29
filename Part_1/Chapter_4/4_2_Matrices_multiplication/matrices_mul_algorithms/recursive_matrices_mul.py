import numpy as np
from .utils import print_matrix, pad_matrix_with_zeros_to_square, get_product_of_matrix_symmetric_2d_partition


def multiply_matrices_recursive(a: np.array, b: np.array) -> np.array:
    c_res_rows_num, c_res_cols_num = len(a), len(b[0])
    a, b = pad_matrix_with_zeros_to_square(a), pad_matrix_with_zeros_to_square(b)

    def _multiply_matrices_recursive(_a: np.array, _b: np.array) -> np.array:
        size = len(_a)
        if size == 1:
            _c = _a * _b
        else:
            a11, a12, a21, a22 = get_product_of_matrix_symmetric_2d_partition(_a)
            b11, b12, b21, b22 = get_product_of_matrix_symmetric_2d_partition(_b)

            half_size = size // 2

            _c = np.zeros((size, size))
            _c[:half_size, :half_size] = _multiply_matrices_recursive(a11, b11) + _multiply_matrices_recursive(a12, b21)
            _c[:half_size, half_size:] = _multiply_matrices_recursive(a11, b12) + _multiply_matrices_recursive(a12, b22)
            _c[half_size:, :half_size] = _multiply_matrices_recursive(a21, b11) + _multiply_matrices_recursive(a22, b21)
            _c[half_size:, half_size:] = _multiply_matrices_recursive(a21, b12) + _multiply_matrices_recursive(a22, b22)
        return _c

    c_res = _multiply_matrices_recursive(a, b)
    return c_res[:c_res_rows_num, :c_res_cols_num]


if __name__ == '__main__':
    A = np.array(
        [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5]
        ]
    )
    B = np.array(
        [
            [5, 5, 5, 5],
            [4, 4, 4, 4],
            [3, 3, 3, 3],
            [2, 2, 2, 2],
            [1, 1, 1, 1]
        ]
    )

    C_np = A @ B
    print('Numpy mul function:')
    print_matrix(C_np)

    C = multiply_matrices_recursive(A, B)
    print('Recursive mul function:')
    print_matrix(C)

    matrices_equality = np.all(C_np == C)
    print(f'Mareices equality: {matrices_equality}')
