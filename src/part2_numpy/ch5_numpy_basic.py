import numpy as np

## Splitting array

list1: list = [i for i in range(10)]
print(list1)

arr: np.ndarray = np.array(list1)
arr_list: list[np.ndarray] = np.split(arr, 2)  # split into 2 arrays (2 rows)
for i in arr_list:
    print(i)
