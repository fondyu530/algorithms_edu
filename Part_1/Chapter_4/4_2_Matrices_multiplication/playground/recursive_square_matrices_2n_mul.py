from matrices_multiplication import initialize_empty_mat_mul_product, print_matrix, multiply_matrices


def multiply_matrices_recursive(
        a: list[list[float]],
        b: list[list[float]],
        start_row_a_ind: int,
        end_row_a_ind: int,
        start_col_a_ind: int,
        end_col_a_ind: int,
        start_row_b_ind: int,
        end_row_b_ind: int,
        start_col_b_ind: int,
        end_col_b_ind: int
) -> None:
    global C

    if start_row_a_ind == end_row_a_ind:
        C[start_row_a_ind][start_col_b_ind] += a[start_row_a_ind][start_col_a_ind] * b[start_row_b_ind][start_col_b_ind]
    else:
        multiply_matrices_recursive(
            a,
            b,
            start_row_a_ind,
            (end_row_a_ind + start_row_a_ind) // 2,
            start_col_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2,
            start_row_b_ind,
            (end_row_b_ind + start_row_b_ind) // 2,
            start_col_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2
        )

        multiply_matrices_recursive(
            a,
            b,
            start_row_a_ind,
            (end_row_a_ind + start_row_a_ind) // 2,
            (end_col_a_ind + start_col_a_ind) // 2 + 1,
            end_col_a_ind,

            (start_row_b_ind + end_row_b_ind) // 2 + 1,
            end_row_b_ind,
            start_col_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2
        )

        multiply_matrices_recursive(
            a,
            b,
            start_row_a_ind,
            (end_row_a_ind + start_row_a_ind) // 2,
            start_col_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2,

            start_row_b_ind,
            (end_row_b_ind + start_row_b_ind) // 2,
            (end_col_b_ind + start_col_b_ind) // 2 + 1,
            end_col_b_ind
        )

        multiply_matrices_recursive(
            a,
            b,
            start_row_a_ind,
            (end_row_a_ind + start_row_a_ind) // 2,
            (end_col_a_ind + start_col_a_ind) // 2 + 1,
            end_col_a_ind,

            (start_row_b_ind + end_row_b_ind) // 2 + 1,
            end_row_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2 + 1,
            end_col_b_ind
        )

        multiply_matrices_recursive(
            a,
            b,
            (start_row_a_ind + end_row_a_ind) // 2 + 1,
            end_row_a_ind,
            start_col_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2,

            start_row_b_ind,
            (end_row_b_ind + start_row_b_ind) // 2,
            start_col_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2
        )

        multiply_matrices_recursive(
            a,
            b,
            (start_row_a_ind + end_row_a_ind) // 2 + 1,
            end_row_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2 + 1,
            end_col_a_ind,

            (start_row_b_ind + end_row_b_ind) // 2 + 1,
            end_row_b_ind,
            start_col_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2
        )

        multiply_matrices_recursive(
            a,
            b,
            (start_row_a_ind + end_row_a_ind) // 2 + 1,
            end_row_a_ind,
            start_col_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2,

            start_row_b_ind,
            (end_row_b_ind + start_row_b_ind) // 2,
            (end_col_b_ind + start_col_b_ind) // 2 + 1,
            end_col_b_ind
        )

        multiply_matrices_recursive(
            a,
            b,
            (start_row_a_ind + end_row_a_ind) // 2 + 1,
            end_row_a_ind,
            (end_col_a_ind + start_col_a_ind) // 2 + 1,
            end_col_a_ind,

            (start_row_b_ind + end_row_b_ind) // 2 + 1,
            end_row_b_ind,
            (end_col_b_ind + start_col_b_ind) // 2 + 1,
            end_col_b_ind
        )

        # multiply_matrices_recursive(a, b, start_row_ind, (end_row_ind + start_row_ind) // 2, start_col_ind, (end_col_ind + start_col_ind) // 2)

        # multiply_matrices_recursive(a, b, start_row_ind, (end_row_ind + start_row_ind) // 2, (end_col_ind + start_col_ind) // 2 + 1, end_col_ind)

        # multiply_matrices_recursive(a, b, (start_row_ind + end_row_ind) // 2 + 1, end_row_ind, start_col_ind, (end_col_ind + start_col_ind) // 2)

        # multiply_matrices_recursive(a, b, (start_row_ind + end_row_ind) // 2 + 1, end_row_ind, (end_col_ind + start_col_ind) // 2 + 1, end_col_ind)


if __name__ == '__main__':
    A = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]

    B = [
        [4, 4, 4, 4],
        [3, 3, 3, 3],
        [2, 2, 2, 2],
        [1, 1, 1, 1]
    ]

    # C = [
    #     [1, 10, 100, 1000, 2, 20, 200, 2000],
    #     [10, 10, 100, 1000, 20, 20, 200, 2000],
    #     [100, 100, 100, 1000, 200, 200, 200, 2000],
    #     [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    #     [3, 30, 300, 3000, 4, 40, 400, 4000],
    #     [30, 30, 300, 3000, 40, 40, 400, 4000],
    #     [300, 300, 300, 3000, 400, 400, 400, 4000],
    #     [3000, 3000, 3000, 3000, 4000, 4000, 4000, 4000]
    # ]

    C = multiply_matrices(A, B)
    print('General mul function:')
    print_matrix(C)

    C = initialize_empty_mat_mul_product(A, B)
    multiply_matrices_recursive(A, B, 0, len(C) - 1, 0, len(C[0]) - 1, 0, len(C) - 1, 0, len(C[0]) - 1)
    print('Recursive mul function:')
    print_matrix(C)
