import numpy as np
import pandas as pd
## Creating numpy array from list

print("=" * 80)
print("Creating numpy array from list")

# create list by using list comprehension
lis1: list = [i for i in range(10)]
print(f"lis1: {lis1}")

# create numpy array from list
arr1: np.ndarray = np.array(lis1)
print(f"arr1: {arr1}")

# Create 2-dimensional array from list of lists
print("=" * 80)
print(f"Create 2-dimensional array from list of lists")
list2:list=[i for i in range(5) for j in range(5)]
print(f"list2: {list2}")

arr2:np.ndarray=np.array(list2).reshape(5,5)
print(f"arr2: {arr2}")

## Creating array from scratch
print("=" * 80)
print(f"Creating array from scratch")
zeros_array:np.ndarray = np.zeros((3, 4))
print(f"zeros_array: {zeros_array}")

ones_array: np.ndarray = np.ones((3, 4))
print(f"ones_array: {ones_array}")

filled_array:np.ndarray = np.full((3, 4), 5)
print(f"filled_array: {filled_array}")

arrange_array:np.ndarray = np.arange(0, 20, 2)
print(f"arrange_array: {arrange_array}")

linspace_array:np.ndarray = np.linspace(0, 1, 5)
print(f"linspace_array: {linspace_array}")

random_array:np.ndarray = np.random.random((3, 4))
print(f"random_array: {random_array}")

normal_random_array:np.ndarray = np.random.normal(0, 1, (3, 4))
print(f"normal_random_array: {normal_random_array}")

random_int_array:np.ndarray = np.random.randint(0, 10, (3, 4))
print(f"random_int_array: {random_int_array}")

identity_matrix:np.ndarray = np.eye(3)
print(f"identity_matrix: {identity_matrix}")

empty_array:np.ndarray = np.empty(3)
print(f"empty_array: {empty_array}")
