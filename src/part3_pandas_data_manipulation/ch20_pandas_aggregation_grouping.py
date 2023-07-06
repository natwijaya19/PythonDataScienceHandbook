"""
ch20_pandas_aggregation grouping
"""
import numpy as np
import pandas as pd
import seaborn as sns  # type: ignore
from numpy.random import RandomState


# helper functions
def create_borderline():
    print("=" * 80)


## Planet Data in a seaborn library
planets: pd.DataFrame = sns.load_dataset("planets")
print(planets.head())

## Split, Apply, Combine

df: pd.DataFrame = pd.DataFrame(
    {'key': ['A', 'B', 'C', 'A', 'B', 'C'],
     'data': range(6), },
    columns=['key', 'data']
)
print(f"df:\n{df}")

groupby_key: pd.DataFrame = df.groupby('key').sum()
print(f"groupby_key:\n{groupby_key}")

# Group planets by method
# Calculate mean of meas of each group planet
planets_method_group_mean = planets.groupby('method')['mass'].mean()
print(f"planets_method_group_mean:\n{planets_method_group_mean}")

# Group planets by method
# Calculate a mean orbital period of each group planet
planets_methodgroup_orbitalperiod = planets.groupby('method')['orbital_period'].mean()
print(f"planets_methodgroup_orbitalperiod:\n{planets_methodgroup_orbitalperiod}")

# Iteration over groups
print(f"Iteration over groups:")
for (method, group) in planets.groupby('method'):
    print(f"{method:30} shape={group.shape}")

# Dispatch methods
planets_grouped_describe = planets.groupby('method')['year'].describe()
print(f"planets_grouped_describe:\n{planets_grouped_describe}")

planets_grouped_describe_stack = planets_grouped_describe.stack()
print(f"planets_grouped_describe_stack:\n{planets_grouped_describe_stack}")

planets_grouped_describe_unstack = planets_grouped_describe.unstack()
print(f"planets_grouped_describe_unstack:\n{planets_grouped_describe_unstack}")

## Aggregate, filter, transform, apply
rng: np.random.RandomState = np.random.RandomState(0)
df = pd.DataFrame(
    {
        'key': ['A', 'B', 'C', 'A', 'B', 'C'],
        'data1': range(6),
        'data2': rng.randint(0, 10, 6),
    },
    columns=['key', 'data1', 'data2']
)
print(f"df:\n{df}")

# aggregation
df_aggreg = df.groupby('key').aggregate(['min', np.median, max])
print(f"df_aggreg:\n{df_aggreg}")


# filtering
def filter_func(x: pd.DataFrame, threshold: int):
    result = x['data2'].std() > threshold
    return result


df_filter = df.groupby('key').filter(filter_func, threshold=4)
print(f"df_filter:\n{df_filter}")


# transformation
def center_func(x: pd.DataFrame):
    result = x - x.mean()
    return result


df_transform = df.groupby('key').transform(center_func)
print(f"df_transform:\n{df_transform}")

df_data = df[['data1', 'data2']]
df_center = df_data.transform(lambda x: x - x.mean())
print(f"df_center:\n{df_center}")


# apply method
def norm_by_data2(x: pd.DataFrame):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x


df_apply_norm: pd.DataFrame = df.groupby('key').apply(norm_by_data2)
print(f"df_apply:\n{df_apply_norm}")

df_apply_mean: pd.DataFrame = df.groupby('key').apply(lambda x: x.mean())
print(f"df_apply_mean:\n{df_apply_mean}")

print(df.groupby('key').aggregate(lambda x: x.mean()))

## Grouping example
planets_df: pd.DataFrame = sns.load_dataset('planets')
decade_number = 10 * (planets['year'] // 10)
decade_str = decade_number.astype(str) + 's'
decade_str.name = 'decade'

planets_groupby_sum: pd.DataFrame = planets_df.groupby(['method', decade_str])['number'].sum()
print(f"planets_groupby_sum:\n{planets_groupby_sum}")

planets_groupby_sum_unstack = planets_groupby_sum.unstack().fillna(0)
print(f"planets_groupby_sum_unstack:\n{planets_groupby_sum_unstack}")
