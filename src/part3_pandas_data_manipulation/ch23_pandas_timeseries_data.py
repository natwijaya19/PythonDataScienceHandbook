"""
ch23 pandas timeseries data
"""
from datetime import datetime

import pandas as pd
import seaborn as sns  # type: ignore
from pandas import PeriodIndex, Series, DatetimeIndex


# helper functions
def create_borderline():
    print("=" * 80)


## Indexing by time
index = pd.DatetimeIndex(
    ["2017-07-04", "2017-08-04", "2018-07-04", "2018-08-04"]
)
data = pd.Series([0, 1, 2, 3], index=index, name="data")
print(data)

# Slice by date
sliced_by_date = data["2017-07-04":"2018-07-04"]
print(f"sliced_by_date: \n{sliced_by_date}")
create_borderline()

# Partial string indexing
sliced_by_year: Series = data["2017"]
print(f"sliced_by_year: \n{sliced_by_year}")

create_borderline()

## Pandas datetime data structures
# create dDatetimeIndex by using pd.to_datetime()
dates: DatetimeIndex | Series = pd.to_datetime([
    datetime(year=2015, month=7, day=3),
    "4th of July, 2021",
    '2022-Jul-6',
    '07-08-2022',
    '2022/12/08',
    '20221211',
])
print(dates)

# convert to period
periods: PeriodIndex | Series = dates.to_period('D')
print(periods)

# Create timedelta by subtraction
timedeltas: pd.TimedeltaIndex = dates - dates[0]
print(timedeltas)

## Regular sequence
# create regular sequence by using pd.date_range()
# default freq is 'D'
# Provide start and end date parameters
dateranges1: pd.DatetimeIndex = pd.date_range(start='2021-07-03',
                                              end='2021-07-10'
                                              )
print(f"dateranges1: \n{dateranges1}")

# Provide start and periods parameters
dateranges2: pd.DatetimeIndex = pd.date_range(start='2021-07-03',
                                              periods=8
                                              )
print(f"dateranges2: \n{dateranges2}")

# Use freq parameter
dateranges3: pd.DatetimeIndex = pd.date_range(start='2021-07-03',
                                              periods=8,
                                              freq='H'
                                              )
print(f"dateranges3: \n{dateranges3}")

# Create pd.PeriodIndex by using pd.period_range()
periodranges1: pd.PeriodIndex = pd.period_range(start='2021-07-03',
                                                periods=8,
                                                freq='M'
                                                )
print(f"periodranges1: \n{periodranges1}")

# Create pd.TimedeltaIndex by using pd.timedelta_range()
timedeltaranges1: pd.TimedeltaIndex = pd.timedelta_range(start=0,
                                                         periods=8,
                                                         freq='H'
                                                         )
print(f"timedeltaranges1: \n{timedeltaranges1}")

timedeltarange2: pd.TimedeltaIndex = pd.timedelta_range(start=0,
                                                        periods=8,
                                                        freq='7D',
                                                        )
print(f"timedeltarange2: \n{timedeltarange2}")

## Frequencies and offsets
