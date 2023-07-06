"""
Chapter 15: Operating on Data in Pandas
"""

import numpy as np
import pandas as pd

print("=" * 80)

### Pandas DataFrame
# The most populous states in the US by 2022
print(f"{'The most populous states in the US by 2022':*^80}")
states_population_dict: dict = {
    'California': 39512223,
    'Texas': 28995881,
    'New York': 19453561,
    'Florida': 21477737,
    'Illinois': 12671821,
}
states_population_series: pd.Series = pd.Series(states_population_dict)
print(f"states_population_series:\n{states_population_series}")
# The area of the states in the US
print(f"{'The area of the states in the US':*^80}")
states_area_dict: dict = {
    'California': 423967,
    'Texas': 695662,
    'New York': 141297,
    'Florida': 170312,
    'Illinois': 149995,
}
states_area_series: pd.Series = pd.Series(states_area_dict)
print(f"states_area_series:\n{states_area_series}")

## Ufuncs:Index preservation
rng = np.random.default_rng(seed=42)
ser: pd.Series = pd.Series(rng.integers(low=0, high=10, size=4))
print(f"ser:\n{ser}")

data_df: pd.DataFrame = pd.DataFrame(rng.integers(low=0, high=10, size=(3, 4)),
                                     columns=['A', 'B', 'C', 'D'])
print(f"data_df:\n{data_df}")

print("=" * 80)
npexp_ser: pd.Series = np.exp(ser)
print(f"np.exp(ser):\n{npexp_ser}")

print("=" * 80)
npsin_df: pd.DataFrame = np.sin(data_df * np.pi / 4)
print(f"np.sin(data_df * np.pi / 4):\n{npsin_df}")

## Index alignment in series
print("=" * 80)
print(f"{'Index alignment in series':*^80}")
A: pd.Series = pd.Series([2, 4, 6], index=[0, 1, 2])
B: pd.Series = pd.Series([1, 3, 5], index=[1, 2, 3])
C: pd.Series = A + B
print(f"C:\n{C}")
C2: pd.Series = A.add(B, fill_value=0)
print(f"C2:\n{C2}")

## Index alignment in DataFrame
print("=" * 80)
print(f"{'Index alignment in DataFrame':*^80}")
D: pd.DataFrame = pd.DataFrame(rng.integers(low=0, high=20, size=(2, 2)),
                               columns=list('AB'))
print(f"A:\n{D}")

E: pd.DataFrame = pd.DataFrame(rng.integers(low=0, high=10, size=(3, 3)),
                               columns=list('BAC'))
print(f"B:\n{E}")

print("=" * 80)
F: pd.DataFrame = D + E
print(f"C:\n{C}")
G: pd.DataFrame = D.add(E, fill_value=0)
print(f"G:\n{G}")
