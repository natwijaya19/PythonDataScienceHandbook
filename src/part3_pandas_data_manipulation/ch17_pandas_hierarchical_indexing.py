"""
Chapter 15: Operating on Data in Pandas
"""

import numpy as np
import pandas as pd
from pandas import Series
from pandas.core.indexing import _IndexSlice  # type: ignore

print("=" * 80)

## Create multi-indexed Series and DataFrame objects ##
print("Create multi-indexed Series")
state_list: list = [
    "California",
    "New York",
    "Texas", ]

year_list: list = [2010, 2020]

populations_list: list = [
    37_253_956, 39_512_223,
    19_378_102, 20_201_249,
    25_145_561, 29_360_759, ]
print(f"state_list: {state_list}")
print(f"year_list: {year_list}")
print(f"populations_list: {populations_list}\n")

multi_index: pd.MultiIndex = pd.MultiIndex.from_product(
    [state_list, year_list],
    names=["state", "year"])
print(f"multi_index:\n{multi_index}\n")

pop_series: pd.Series = pd.Series(populations_list, index=multi_index)
print(f"populations:\n{pop_series}\n")

pop_df: pd.DataFrame = pop_series.unstack()
print(f"pop_df:\n{pop_df}\n")

pop_stacked: pd.Series = pop_df.stack()
print(f"pop_stacked:\n{pop_stacked}\n")

# Add more column for population under 18 to the dataframe
print("=" * 80)
states_df: pd.DataFrame = pd.DataFrame(
    {"total_pop": pop_series,
     "under_18": [9_071_485, 9_378_587,
                  7_293_731, 7_471_728,
                  8_873_190, 9_943_600, ]},
)
print(f"states_df:\n{states_df}\n")

states_df["under_18_portion"] = states_df["under_18"] / states_df["total_pop"]
print(f"states_df:\n{states_df}\n")

## Multi-index for columns ##
print("=" * 80)
print("Multi-index for columns")
index = pd.MultiIndex.from_product(
    [[2013, 2014], [1, 2]],
    names=["year", "visit"])

columns = pd.MultiIndex.from_product(
    [["Bob", "Guido", "Sue"], ["HR", "Temp"]],
    names=["subject", "type"])

data_array: np.ndarray = np.round(np.random.randn(4, 6), 1)
data_array[:, ::2] *= 10
data_array += 37
print(f"data_array:\n{data_array}\n")

health_data: pd.DataFrame = pd.DataFrame(
    data=data_array,
    index=index,
    columns=columns)
print(f"health_data:\n{health_data}\n")

## Indexing and slicing a multi-indexed Series ##
print("=" * 80)
print("Indexing and slicing a multi-indexed Series")
print(f"pop_series:\n{pop_series}\n")

print(f"pop_series[('California', 2010)]: {pop_series[('California', 2010)]}\n")

print(f"pop_series['California', 2010]: {pop_series['California', 2010]}\n")

calif: Series = pop_series["California"]
print(f"calif:\n{calif}\n")

cal_ny: pd.Series = pop_series["California":"New York"]
print(f"cal_ny:\n{cal_ny}\n")

# filter states with population under 20 million
larger_20mn: pd.Series = pop_series[pop_series > 20_000_000]
print(f"larger_20mn:\n{larger_20mn}\n")

# fancy indexing
cal_tex: pd.Series = pop_series[["California", "Texas"]]
print(f"cal_tex:\n{cal_tex}\n")

## Indexing and slicing a multi-indexed DataFrame ##
print("=" * 80)
print("Indexing and slicing a multi-indexed DataFrame")
print(f"health_data:\n{health_data}\n")

print(f"health_data['Guido', 'HR']:\n{health_data['Guido', 'HR']}\n")
guido: pd.DataFrame = health_data["Guido"]
print(f"guido:\n{guido}\n")

print(f"health_data.iloc[:2, :2]:\n{health_data.iloc[:2, :2]}\n")

print(f"health_data.loc[:, ('Bob', 'HR')]:\n{health_data.loc[:, ('Bob', 'HR')]}\n")

# slice the inner index level by using empty slice `:` directly in the first index position
idx: _IndexSlice = pd.IndexSlice
hr_data: pd.DataFrame = health_data.loc[idx[:, 1], idx[:, 'HR']]
print(f"hr_data:\n{hr_data}\n")

## Rearranging multi-indexed Series and DataFrames ##
print("=" * 80)
print("Rearranging multi-indexed Series and DataFrames")
print(f"pop_series:\n{pop_series}\n")

print(f"pop_series.unstack(level=0):\n{pop_series.unstack(level=0)}\n")

print(f"pop_series.unstack(level=1):\n{pop_series.unstack(level=1)}\n")

print(f"pop_series.unstack(level='state'):\n{pop_series.unstack(level='state')}\n")

print(f"pop_series.unstack(level='year'):\n{pop_series.unstack(level='year')}\n")

print(f"pop_series.unstack().stack():\n{pop_series.unstack().stack()}\n")

print(f"pop_series.unstack().stack(dropna=False):\n{pop_series.unstack().stack(dropna=False)}\n")

## Index setting and resetting ##
print("=" * 80)
print("Index setting and resetting")
print(f"pop_series:\n{pop_series}\n")

pop_df3: pd.DataFrame = pop_series.unstack()
print(f"pop_df3:\n{pop_df3}\n")

pop_flat: pd.DataFrame = pop_series.reset_index(name="population")
print(f"pop_flat:\n{pop_flat}\n")

pop_ser: pd.DataFrame = pop_flat.set_index(["state", "year"])
print(f"pop_ser:\n{pop_ser}\n")
