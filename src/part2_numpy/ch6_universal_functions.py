"""
This module contains the universal functions used in the book.
"""

import numpy as np


## The slowness of Python loops


def compute_reciprocals(value_array: np.ndarray):
    """
    Compute the reciprocal of the values in the given array.
    """
    output = np.empty(len(value_array))
    for i in range(len(value_array)):
        output[i] = 1.0 / value_array[i]
    return output


rng = np.random.default_rng(seed=1701)  # seed for reproducibility

import time

## Small number of elements
start_time = time.time()
values = rng.integers(low=1, high=10, size=5)
compute_reciprocals(values)
time_lapse = time.time() - start_time
print(f"Time elapsed for small number of elements: {time_lapse:.6f} seconds")

## Large number of elements
# start_time = time.time()
# big_array: np.ndarray = rng.integers(low=1, high=100, size=10 ** 7)
# compute_reciprocals(big_array)
# time_lapse = time.time() - start_time
# print(f"Time elapsed for large number of elements: {time_lapse:.6f} seconds")

## Vectorized operations in NumPy
big_array: np.ndarray = rng.integers(low=1, high=100, size=10 ** 6)
start_time = time.time()
1.0 / big_array
time_lapse = time.time() - start_time
print(f"Time elapsed for large number of elements by using vectorized operations: {time_lapse:.6f} seconds")

## Exploring NumPy's UFuncs
x = np.arange(4)
print(f"x = {x}")
print(f"x + 5 = {x + 5}")
print(f"x - 5 = {x - 5}")
print(f"x * 2 = {x * 2}")
print(f"x / 2 = {x / 2}")
print(f"x // 2 = {x // 2}")
print(f"-x = {-x}")
print(f"x ** 2 = {x ** 2}")
print(f"x % 2 = {x % 2}")

print(f"-(0.5 * x + 1) ** 2 = {-(0.5 * x + 1) ** 2}")

print(f"x = {x}")
print(f"np.add(x, 2) = {np.add(x, 2)}")
print(f"np.subtract(x, 2) = {np.subtract(x, 2)}")
print(f"np.multiply(x, 2) = {np.multiply(x, 2)}")

## Sort function
big_array: np.ndarray = rng.integers(low=1, high=100, size=10 ** 6)
sorted_array: np.ndarray = np.sort(big_array)
print(f"big_array = {big_array}")
print(f"sorted_array = {sorted_array}")
