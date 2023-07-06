"""
Chapter 14: Indexing and Selection in Pandas DataFrames and Series Objects
"""

import numpy as np
import pandas as pd

print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print("=" * 80)
### Pandas DataFrame
# The most populous states in the US by 2022
states_population_dict: dict = {
    'California': 39512223,
    'Texas': 28995881,
    'New York': 19453561,
    'Florida': 21477737,
    'Illinois': 12671821,
}

states_area_dict: dict = {
    'California': 423967,
    'Texas': 695662,
    'New York': 141297,
    'Florida': 170312,
    'Illinois': 149995,
}

population_series: pd.Series = pd.Series(states_population_dict)
area_series: pd.Series = pd.Series(states_area_dict)

states_df: pd.DataFrame = pd.DataFrame({
    'population': population_series,
    'area': area_series
})

print(f"states_df:\n{states_df}")

print("=" * 80)
print(f"data_df['area']:\n{states_df['area']}")
print("=" * 80)
print(f"data_df.area:\n{states_df.area}")

print("=" * 80)
print(f"states_df['area'] is states_df.area: {states_df['area'] is states_df.area}")  # True

print("=" * 80)
print(f"type(states_df['area']): {type(states_df['area'])}")  # Series

# Adding new series: population density (people per square mile)
print("=" * 80)
print(f"Adding new series: population density (people per square mile)")
states_df['density'] = states_df['population'] / states_df['area']
print(f"states_df:\n{states_df}")

print("=" * 80)
# Transpose the DataFrame
print(f"states_df.T:\n{states_df.T}")
# The Original DataFrame is not affected
print(f"states_df:\n{states_df}")

# Indexing by using iloc implicit integer index and loc explicit index
print("=" * 80)
print(f"Indexing by using iloc implicit integer index and loc explicit index")
print(f"states_df.iloc[:3, :2]:\n{states_df.iloc[:3, :2]}")
print("=" * 80)
print(f"states_df.loc[:'New York', :'area']:\n{states_df.loc[:'New York', :'area']}")

# Using masking to filter data
print("=" * 80)
print(f"Using masking to filter data")
print(f"states_df.loc[states_df.density > 100, ['population', 'density']]:\n"
      f"{states_df.loc[states_df.density > 100, ['population', 'density']]}")

# Modifying values
print("=" * 80)
print(f"Modifying values")
states_df.iloc[0, 2] = 90
print(f"states_df:\n{states_df}")


## Additional conventions for indexing
# Indexing refers to columns, slicing refers to rows
print("=" * 80)
print(f"Slicing")
print(f"states_df['Texas':'New York']:\n{states_df['Texas':'New York']}")

print("=" * 80)
print(f"Indexing")
print(f"states_df[1:3]:\n{states_df[1:3]}")

print(f"Row wise operations on masking")
# Filter data with density > 100
print(f"states_df[states_df.density > 100]:\n{states_df[states_df.density > 100]}")
