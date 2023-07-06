import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd
import seaborn  # type: ignore

rainfall_data_df: pd.DataFrame = pd.read_csv('data/Seattle2014.csv')
rainfall_data_df.set_index('DATE', inplace=True)
print(rainfall_data_df.head())

prcp_array: np.ndarray = rainfall_data_df['PRCP']
print(prcp_array)

seaborn.set()  # set plot styles

plt.hist(prcp_array, 40)
plt.title('Seattle 2014 Precipitation')
plt.xlabel('Precipitation (in)')
plt.ylabel('Number of days')
plt.show()
