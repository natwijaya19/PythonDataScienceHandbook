"""
ch21_pandas_pivot_tables.py
"""
import pandas as pd
import seaborn as sns  # type: ignore


# helper functions
def create_borderline():
    print("=" * 80)


## Titanic dataset from seaborn
titanic_df = sns.load_dataset("titanic")
print(titanic_df.head())
create_borderline()

# survival rate by sex
survived_df_mean = titanic_df.groupby("sex")[["survived"]].mean()
print(f"survived_df: {survived_df_mean}")
create_borderline()

survived_df_count = titanic_df.groupby("sex")["survived"].count()
print(f"survived_df: {survived_df_count}")

# survival rate by sex and by class in a two-dimensional table
survive_sex_class: pd.DataFrame = titanic_df.groupby(["sex", "class"])["survived"].aggregate("mean").unstack()
print(f"survive_sex_class: \n{survive_sex_class}")

## Pivot table syntax
survive_sex_class_pivot: pd.DataFrame = titanic_df.pivot_table(
    values="survived",
    index="sex",
    columns="class",
    aggfunc="mean",
)
print(f"survive_sex_class_pivot: \n{survive_sex_class_pivot}")

## Multi-level pivot tables
age: pd.Series = pd.cut(
    x=titanic_df["age"],
    bins=[0, 18, 25, 99],
    labels=["child", "young adult", "adult"],
)

survival_sex_age_class: pd.DataFrame = titanic_df.pivot_table(
    values="survived",
    index=["sex", age],
    columns="class",
    aggfunc="mean",
)
print(f"survival_sex_age_class: \n{survival_sex_age_class}")

## Additional pivot table options
survival_sex_age_class_fare = titanic_df.pivot_table(
    index=["sex", age],
    columns="class",
    aggfunc={"survived": "mean", "fare": "mean"},
)

print(f"survival_sex_age_class_fare: \n{survival_sex_age_class_fare}")

# pivot table along with totals
survival_sex_class_total= titanic_df.pivot_table(
    values="survived",
    index="sex",
    columns="class",
    aggfunc="mean",
    margins=True,
)

print(f"survival_sex_class_total: \n{survival_sex_class_total}")

## Example: Birthrate data
