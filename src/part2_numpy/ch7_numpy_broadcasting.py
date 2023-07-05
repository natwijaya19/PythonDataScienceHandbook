import numpy as np

a: np.ndarray = np.arange(3)
b: np.ndarray = np.array([5, 5, 5])

print(f"a: {a}")
print(f"b: {b}")
print(f"a + b: {a + b}")
print(f"a + 5: {a + 5}")

M: np.ndarray = np.ones((3, 3))
print(f"M: {M}")
print(f"M + a: {M + a}")

## Plot two-dimensional function
# x and y have 50 steps from 0 to 5
x: np.ndarray = np.linspace(0, 5, 50)
y: np.ndarray = np.linspace(0, 5, 50)[:, np.newaxis]
z: np.ndarray = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

import matplotlib.pyplot as plt

plt.imshow(z, origin="lower", extent=[0, 5, 0, 5], cmap="viridis")
plt.colorbar()
plt.show()
