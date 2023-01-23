# Import the required libraries
from scipy import linalg
import numpy as np

# 7x + 2y = 8
# 4x + 5y = 10

# The function takes two arrays
a = np.array([[7, 2], [4, 5]])
b = np.array([8, 10])

# Solving the linear equations
res = linalg.solve(a, b)
print(res)
