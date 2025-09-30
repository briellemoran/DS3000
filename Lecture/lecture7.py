import numpy as np
import sympy as sp

# Lecture 7, Python Classwork

# What amount of effort would you need to put into each aspect to achieve your goal?
# Which aspects should you focus on more? -> gain an intuitive understanding 
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [0, 0, 1]])
a = np.array([72, 84, 20])
print(np.linalg.solve(A, a))

# Practice Linear Dependence
B = np.array([[1, 0, 0],
              [2, 1, 1],
              [3, 4, 1],
              [1, 0, 1]])
b = np.array([2, 0, 1])
print(np.linalg.solve(B, b))