import numpy as np
import sympy as sp

# Verify this equation
a = np.array([[1.5], [2.598]])
c = np.array([[-1.964], [4.598]])

aNorm = a / np.linalg.norm(a, ord=2)
cNorm = c / np.linalg.norm(c, ord=2)

print(np.arccos(np.dot(aNorm.T, cNorm)))