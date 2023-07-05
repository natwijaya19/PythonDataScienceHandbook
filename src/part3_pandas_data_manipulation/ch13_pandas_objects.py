import numpy as np
import pandas as pd
from numpy import ndarray
from pandas import RangeIndex, Index

print(pd.__version__)
print(np.__version__)

## pandas series
# create series from a list
list1: list = [(i + 1) / 4 for i in range(4)]
data_series: pd.Series = pd.Series(list1)
print(f"data: {data_series}")

data_values: np.ndarray = data_series.values
print(f"data_values: {data_values}")

data_numpy_array: np.ndarray = np.array(data_series)
print(f"data_numpy: {data_numpy_array}")

data_index: RangeIndex = data_series.index
print(f"data_index: {data_index}")

# The most populous states in the US
states_population: dict = {"California": 38332521,
                           "Texas": 26448193,
                           "New York": 19651127,
                           "Florida": 19552860,
                           "Illinois": 12882135,
                           "Pennsylvania": 12773801,
                           "Ohio": 11570808,
                           "Georgia": 9992167,
                           "Michigan": 9895622,
                           "North Carolina": 9848060,
                           }

states_population_series: pd.Series = pd.Series(states_population)
print(f"states_population_series: {states_population_series}")

## pandas dataframe
# create dataframe from a list
list2: list = [(i + 1) / 4 for i in range(4)]
list3: list = ["a", "b", "c", "d"]
data_df: pd.DataFrame = pd.DataFrame(list(zip(list2, list3)), columns=["col1", "col2"])
print(f"data_df:")
print(data_df)
data_df_values: ndarray = data_df.values
print(f"data_df_values: {data_df_values}")

data_df_index: RangeIndex = data_df.index
print(f"data_df_index: {data_df_index}")

data_df_column: Index = data_df.columns
print(f"data_df_column: {data_df_column}")

col1_data: pd.Series = data_df["col1"]
print(f"col1_data: {col1_data}")

## more on pandas dataframe
# The most populous states in the US
states_population: dict = {"California": 38332521,
                           "Texas": 26448193,
                           "New York": 19651127,
                           "Florida": 19552860,
                           "Illinois": 12882135,
                           "Pennsylvania": 12773801,
                           "Ohio": 11570808,
                           "Georgia": 9992167,
                           "Michigan": 9895622,
                           "North Carolina": 9848060,
                           }

# Are of the states in the US
states_area: dict = {"California": 423967,
                     "Texas": 695662,
                     "New York": 141297,
                     "Florida": 170312,
                     "Illinois": 149995,
                     "Pennsylvania": 119995,
                     "Ohio": 114995,
                     "Georgia": 9992167,
                     "Michigan": 9895622,
                     "North Carolina": 9848060,
                     }

# Create dataframe from pandas series
states_population_series2: pd.Series = pd.Series(states_population)
states_population_df: pd.DataFrame = pd.DataFrame(states_population_series2, columns=["population"])
print(f"states_population_df: \n{states_population_df}")

## Pandas dataframe from a list of dictionaries
data_list_dict: list[dict] = [{"a": i, "b": 2 * i} for i in range(3)]
print(f"data_list: \n{data_list_dict}")
data_df2: pd.DataFrame = pd.DataFrame(data_list_dict)
print(f"data_df2: \n{data_df2}")

## Pandas dataframe from a dictionary of series objects
state_population_series: pd.Series = pd.Series(states_population)
state_area_series: pd.Series = pd.Series(states_area)
states_df: pd.DataFrame = pd.DataFrame({"population": state_population_series, "area": state_area_series})
print(f"states_df: \n{states_df}")


