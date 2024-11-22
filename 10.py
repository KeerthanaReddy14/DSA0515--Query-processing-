import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
def print_colored_df(dataframe):
    for index, row in dataframe.iterrows():
        formatted_row = [
            f"\033[91m{val:.2f}\033[0m" if val < 0 else f"\033[90m{val:.2f}\033[0m"
            for val in row
        ]
        print(" | ".join(formatted_row))
print("Negative numbers (marked):")
print(df[df < 0].fillna('NEGATIVE'))
print("\nPositive numbers (marked):")
print(df[df >= 0].fillna('POSITIVE'))
