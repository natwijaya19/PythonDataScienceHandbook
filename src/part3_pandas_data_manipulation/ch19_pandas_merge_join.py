"""
ch19_pandas_merge_join
"""
from typing import Union

import pandas as pd


# helper functions
def create_borderline():
    print("=" * 80)


def make_df(cols: Union[list, str], ind: list) -> pd.DataFrame:
    """Quickly make a DataFrame"""
    data: dict = {c: [str(c) + str(i) for i in ind]
                  for c in cols}
    data_df = pd.DataFrame(data, ind)
    return data_df


## Example: US States Data
create_borderline()
print("Example: US States Data")

pop = pd.read_csv('../data/state-population.csv')
areas = pd.read_csv('../data/state-areas.csv')
abbrevs = pd.read_csv('../data/state-abbrevs.csv')

print(f"pop.head():\n{pop.head()}")
print(f"areas.head():\n{areas.head()}")
print(f"abbrevs.head():\n{abbrevs.head()}")

# merge pop and abbrevs based on state/region column of pop and abbreviation column of abbrevs
merged = pd.merge(pop, abbrevs, how='outer',
                  left_on='state/region', right_on='abbreviation')
print(f"merged.head():\n{merged.head()}")

# Drop duplicate info (abbreviation column)
merged = merged.drop('abbreviation', axis=1)
print(f"merged.head():\n{merged.head()}")

# Check if any of the rows have nulls
print(f"merged.isnull().any():\n{merged.isnull().any()}")

print(merged[merged['state'].isnull()]['state/region'].unique())
# PR and USA are not valid states because they are not in the abbrevs DataFrame

# Fill the null values with the correct state names
df = merged[merged['state/region'] == 'PR']['state']
print(df)

df1 = merged.loc[merged['state/region'] == 'PR', 'state']
print(df1)

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
print(merged.isnull().any())

# Merge the result with the areas DataFrame using the state column of merged
# and the area (the common column)
final = pd.merge(merged, areas, on='state', how='left')
print(final.head())

# Check if there are any nulls
print(final.isnull().any())

# Check which regions are null
print(final[final['area (sq. mi)'].isnull()]['state'].unique())

# Drop the null values and check if there are any nulls
final.dropna(inplace=True)
print(final.isnull().any())

# Check the data types of the columns
print(final.dtypes)

# filter data in 2010
data2010 = final[final['year'] == 2010][final['ages'] == 'total']
print(data2010.head())

# set the index to state
data2010.set_index('state', inplace=True)
print(data2010.head())

# compute the population density and display it in descending order
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
print(density.head())

# check the most dense states
print(f"density.head():\n{density.head()}")

# check the least dense states
print(f"density.tail():\n{density.tail()}")
