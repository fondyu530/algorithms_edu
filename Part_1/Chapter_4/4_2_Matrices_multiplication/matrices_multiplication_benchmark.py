import time
import numpy as np
import pandas as pd
import plotly.express as px

from matrices_mul_algorithms import (
    multiply_matrices,
    multiply_matrices_strassen,
    multiply_matrices_recursive,
    multiply_matrices_recursive_optimal,
)


if __name__ == '__main__':
    mat_mul_functions = {
        'numpy': np.matmul,
        'general': multiply_matrices,
        'strassen': multiply_matrices_strassen,
        'recursive': multiply_matrices_recursive,
        'recursive_opt': multiply_matrices_recursive_optimal
    }

    df = pd.DataFrame()
    for power in range(8):
        matrix_size = 2 << power
        print(f'Current matrix size: {matrix_size}')

        A = np.random.randint(low=10, size=(matrix_size, matrix_size))
        B = np.random.randint(low=10, size=(matrix_size, matrix_size))

        for algorithm, mat_mul_func in mat_mul_functions.items():
            print(f'Current algorithm: {algorithm}')
            tic = time.time()
            C = mat_mul_func(A, B)
            toc = time.time()

            print(f'Result is correct: {np.all(C == A @ B)}')
            tmp_df = pd.DataFrame(
                {
                    'algorithm': [algorithm],
                    'matrix_size': [matrix_size],
                    'mul_time': [toc - tic]
                }
            )

            df = pd.concat([df, tmp_df])
        print()

    fig = px.line(df, x='matrix_size', y='mul_time', color='algorithm')
    fig.show()
