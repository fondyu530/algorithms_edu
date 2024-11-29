import numpy as np
from .utils import initialize_empty_mat_mul_product, print_matrix


def multiply_matrices(a: np.array, b: np.array) -> np.array:
    c = initialize_empty_mat_mul_product(a, b)

    for i in range(len(c)):
        for j in range(len(c[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c


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

    C = multiply_matrices(A, B)
    print('General mul function:')
    print_matrix(C)

    matrices_equality = np.all(C_np == C)
    print(f'Mareices equality: {matrices_equality}')
