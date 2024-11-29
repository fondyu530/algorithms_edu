import numpy as np

from general_matrices_mul import multiply_matrices
from utils import (
    print_matrix,
    pad_matrix_with_zeros_to_square,
    get_product_of_matrix_symmetric_2d_partition
)


def multiply_matrices_strassen(a: np.array, b: np.array) -> np.array:
    c_res_rows_num, c_res_cols_num = len(a), len(b[0])
    a, b = pad_matrix_with_zeros_to_square(a), pad_matrix_with_zeros_to_square(b)

    def _multiply_matrices_strassen(_a: np.array, _b: np.array) -> np.array:
        size = len(_a)
        _c = np.zeros((size, size))

        if size == 1:
            _c[0][0] = _a[0][0] * _b[0][0]
        else:
            a11, a12, a21, a22 = get_product_of_matrix_symmetric_2d_partition(_a)
            b11, b12, b21, b22 = get_product_of_matrix_symmetric_2d_partition(_b)

            half_size = size // 2

            p1 = _multiply_matrices_strassen(a11, b12 - b22)
            p2 = _multiply_matrices_strassen(a11 + a12, b22)
            p3 = _multiply_matrices_strassen(a21 + a22, b11)
            p4 = _multiply_matrices_strassen(a22, b21 - b11)
            p5 = _multiply_matrices_strassen(a11 + a22, b11 + b22)
            p6 = _multiply_matrices_strassen(a12 - a22, b21 + b22)
            p7 = _multiply_matrices_strassen(a11 - a21, b11 + b12)

            assign_sub_matrix(m=_c, m_sub=p5 + p4 - p2 + p6, start_row_ind=0, start_col_ind=0)
            assign_sub_matrix(m=_c, m_sub=p1 + p2, start_row_ind=0, start_col_ind=half_size)
            assign_sub_matrix(m=_c, m_sub=p3 + p4, start_row_ind=half_size, start_col_ind=0)
            assign_sub_matrix(m=_c, m_sub=p5 + p1 - p3 -p7, start_row_ind=half_size, start_col_ind=half_size)
        return _c
    c_res = _multiply_matrices_strassen(a, b)
    return c_res[:c_res_rows_num, :c_res_cols_num]


def assign_sub_matrix(
        m: np.array,
        m_sub: np.array,
        start_row_ind: int = 0,
        start_col_ind: int = 0
) -> None:
    for i in range(m_sub.shape[0]):
        for j in range(m_sub.shape[1]):
            m[start_row_ind+i][start_col_ind+j] = m_sub[i][j]


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

    C = multiply_matrices(A, B)
    print('General mul function:')
    print_matrix(C)

    C = multiply_matrices_strassen(A, B)
    print('Recursive mul function:')
    print_matrix(C)
