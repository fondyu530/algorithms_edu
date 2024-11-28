from matrices_mul import multiply_matrices
from utils import (
    print_matrix,
    sum_matrices,
    get_matrix_dims,
    pad_matrix_with_zeros_to_square,
    get_product_of_matrix_symmetric_2d_partition
)


def multiply_matrices_recursive(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    c_res_rows_num, c_res_cols_num = len(a), len(b[0])
    a, b = pad_matrix_with_zeros_to_square(a), pad_matrix_with_zeros_to_square(b)

    def _multiply_matrices_recursive(_a: list[list[float]], _b: list[list[float]]) -> list[list[float]]:
        size = len(_a)
        _c = [[0 for _ in range(size)] for _ in range(size)]

        if size == 1:
            _c[0][0] = _a[0][0] * _b[0][0]
        else:
            a11, a12, a21, a22 = get_product_of_matrix_symmetric_2d_partition(_a)
            b11, b12, b21, b22 = get_product_of_matrix_symmetric_2d_partition(_b)

            half_size = size // 2

            assign_sub_matrix(
                m=_c,
                m_sub=sum_matrices(
                    _multiply_matrices_recursive(a11, b11),
                    _multiply_matrices_recursive(a12, b21)
                ),
                start_row_ind=0,
                start_col_ind=0
            )
            assign_sub_matrix(
                m=_c,
                m_sub=sum_matrices(
                    _multiply_matrices_recursive(a11, b12),
                    _multiply_matrices_recursive(a12, b22)
                ),
                start_row_ind=0,
                start_col_ind=half_size
            )
            assign_sub_matrix(
                m=_c,
                m_sub=sum_matrices(
                    _multiply_matrices_recursive(a21, b11),
                    _multiply_matrices_recursive(a22, b21)
                ),
                start_row_ind=half_size,
                start_col_ind=0
            )
            assign_sub_matrix(
                m=_c,
                m_sub=sum_matrices(
                    _multiply_matrices_recursive(a21, b12),
                    _multiply_matrices_recursive(a22, b22)
                ),
                start_row_ind=half_size,
                start_col_ind=half_size
            )
        return _c

    c_res = _multiply_matrices_recursive(a, b)
    return [[c_res[i][j] for j in range(c_res_cols_num)] for i in range(c_res_rows_num)]


def assign_sub_matrix(
        m: list[list[float]],
        m_sub: list[list[float]],
        start_row_ind: int = 0,
        start_col_ind: int = 0
) -> None:
    m_sub_dims = get_matrix_dims(m_sub)
    for i in range(m_sub_dims[0]):
        for j in range(m_sub_dims[1]):
            m[start_row_ind+i][start_col_ind+j] = m_sub[i][j]


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
