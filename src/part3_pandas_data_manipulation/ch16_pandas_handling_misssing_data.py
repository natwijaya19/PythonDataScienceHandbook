"""
Chapter 15: Operating on Data in Pandas
"""

import numpy as np
import pandas as pd

print("=" * 80)

## Detecting null values

data_ser: pd.Series = pd.Series([1, np.nan, 'hello', None, 3.5, pd.NA, 7])
print(f"data_ser :\n{data_ser}\n")

print(f"data_ser.isnull() :\n{data_ser.isnull()}\n")

print("=" * 80)
number_null: int = data_ser.isnull().sum()
print(f"number_null :\n{number_null}\n")

number_notnull: int = data_ser.notnull().sum()
print(f"number_notnull :\n{number_notnull}\n")

data_notnull = data_ser[data_ser.notnull()]
print(f"data_notnull :\n{data_notnull}\n")

data_isnull = data_ser[data_ser.isnull()]
print(f"data_isnull :\n{data_isnull}\n")

print("=" * 80)
