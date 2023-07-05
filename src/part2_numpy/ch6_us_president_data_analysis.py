import numpy as np
import pandas as pd

data: pd.DataFrame = pd.read_csv("data/president_heights.csv")
print(data.head())
print(data.describe())

heights: np.ndarray = np.array(data["height(cm)"])
print(heights)
print("Mean height: ", heights.mean())
print("Standard deviation: ", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ", heights.max())
print("25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.hist(heights)
plt.title("Height Distribution of US Presidents")
plt.xlabel("height (cm)")
plt.ylabel("number")
plt.show()
