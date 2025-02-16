import numpy as np
import pandas as pd
import plotly.express as px


def biased_random(zero_prob: float = 0.5) -> int:
    zeros_num = int(round(zero_prob, 2) * 100)

    zeros_array = np.zeros(zeros_num, dtype=int)
    ones_array = np.ones(100 - zeros_num, dtype=int)

    array = np.concat([zeros_array, ones_array])
    np.random.shuffle(array)

    return np.random.choice(array)


def non_biased_random(biased_zero_prob: float = 0.5) -> int:
    while True:
        first_res, second_res = biased_random(biased_zero_prob), biased_random(biased_zero_prob)
        if first_res != second_res:
            return first_res


if __name__ == '__main__':
    n_simulations = int(1e3)
    biased_zero_probability = 0.5

    df_dict = {'simulation_num': [], 'simulation_result': []}

    for i in range(n_simulations):
        df_dict['simulation_num'].append(i)
        df_dict['simulation_result'].append(non_biased_random(biased_zero_probability))

    res_df = pd.DataFrame(df_dict)
    res_df = res_df.groupby(by=['simulation_result']).agg(records_count=('simulation_num', 'count')).reset_index()

    fig = px.bar(res_df, x='simulation_result', y='records_count')
    fig.show()
