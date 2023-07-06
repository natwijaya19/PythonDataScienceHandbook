"""
ch 18. pandas concat and append
"""

import numpy as np
import pandas as pd
from pandas.core.indexing import _IndexSlice  # type: ignore


# helper functions
def create_borderline():
    print("=" * 80)


def make_df(cols: int | str, ind: int | str) -> pd.DataFrame:
    """Quickly make a DataFrame"""
    data: dict = {c: [str(c) + str(i) for i in ind]
                  for c in cols}
    df = pd.DataFrame(data, ind)
    return df


## Concatenation by using numpy.concatenate
create_borderline()
print("Concatenation by using numpy.concatenate")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])
xyz = np.concatenate([x, y, z])
print(f"xyz: \n{xyz}")

A = np.array([[1, 2, 3],
              [4, 5, 6]])
AA = np.concatenate([A, A], axis=1)
print(f"AA: \n{AA}")

## Simple concatenation with pd.concat
create_borderline()
print("Simple concatenation with pd.concat for pandas Series")

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
ser3 = pd.concat([ser1, ser2])
print(f"ser1: \n{ser1}")
print(f"ser2: \n{ser2}")
print(f"ser3: \n{ser3}")

create_borderline()
print("Simple concatenation with pd.concat for pandas Dataframe")
# Concatenate pandas DataFrames with default axis=0
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print(f"df1: \n{df1}")
print(f"df2: \n{df2}")
print(f"pd.concat([df1, df2]): \n{pd.concat([df1, df2])}")
print(f"pd.concat([df1, df2], axis=1): \n{pd.concat([df1, df2], axis=1)}")
# Concatenate pandas DataFrames with axis=1 or axis='columns'
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print(f"df3: \n{df3}")
print(f"df4: \n{df4}")
print(f"pd.concat([df3, df4], axis='columns'): \n{pd.concat([df3, df4], axis='columns')}")
print(f"pd.concat([df3, df4], axis=1): \n{pd.concat([df3, df4], axis=1)}")
print(f"pd.concat([df3, df4], axis=0): \n{pd.concat([df3, df4], axis=0)}")

## Duplicate indices
create_borderline()
print("Duplicate indices")
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index  # make duplicate indices!
print(f"x: \n{x}")
print(f"y: \n{y}")
print(f"pd.concat([x, y]): \n{pd.concat([x, y])}")

## Catching the repeats as an error
create_borderline()
print("Catching the repeats as an error")
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print(f"ValueError: {e}")

## Ignoring the index
create_borderline()
print("Ignoring the index")
print(f"pd.concat([x, y], ignore_index=True): \n{pd.concat([x, y], ignore_index=True)}")

## Adding MultiIndex keys
create_borderline()
print("Adding MultiIndex keys")
print(f"pd.concat([x, y], keys=['x', 'y']): \n{pd.concat([x, y], keys=['x', 'y'])}")

## Concatenation with joins
create_borderline()
print("Concatenation with joins")
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
print(f"df5: \n{df5}")
print(f"df6: \n{df6}")
print(f"pd.concat([df5, df6]): \n{pd.concat([df5, df6])}")

print(f"pd.concat([df5, df6], join='inner'): \n{pd.concat([df5, df6], join='inner')}")

