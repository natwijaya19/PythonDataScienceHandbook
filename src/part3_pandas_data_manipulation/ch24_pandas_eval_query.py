"""
ch23 pandas timeseries data
"""
import time

import numpy as np
import pandas as pd
import seaborn as sns  # type: ignore


# helper functions
def create_borderline():
    print("=" * 80)


## pandas.eval for efficient operations
rng = np.random.default_rng(42)
nrows, ncols = 10 ** 8, 10 ** 2
df1, df2, df3, df4 = (
    pd.DataFrame(
        rng.random((nrows, ncols))
    )
    for i in range(4)
)
# pandas.eval approach
start_time = time.time()
pd.eval('df1 + df2 + df3 + df4')
time_lapsed = time.time() - start_time
print(f"Time lapsed with pandas.eval approach: {time_lapsed}")

# typical pandas approach
start_time = time.time()
df1 + df2 + df3 + df4
time_lapsed = time.time() - start_time
print(f"Time lapsed with pandas approach: {time_lapsed}")


# numpy approach
