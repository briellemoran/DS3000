import numpy as np
import sympy as sp

# Homework 2, Verified Answers in Python

# Problem B1
A = np.array([[1, 1, 1], 
              [2, 3, 1], 
              [1, -1, 2]])
b = np.array([6, 14, 2])
print("Problem B1", np.linalg.solve(A, b))

# Problem B2
B = sp.Matrix([[2, 1, -1, 3],
               [4, -2, 1, 1],
               [-2, 1, 2, 4],])
print("Problem B2", B.rref())

# Problem B3
C = sp.Matrix([[1, -2, 3, 4],
             [2, -4, 6, 8],
             [-1, 2, -3, -4]])
print("Problem B3", C.rref())

# Problem B4
D = sp.Matrix([[1, 2, 3],
              [2, 4, 6]])
print("Problem B4", D.rref())

# Problem B5
E = sp.Matrix([[1, 2, 1, -1, 2],
               [2, 4, 0, 0, 4],
               [-1, -2, 3, 1, 1],
               [3, 6, 1, 0, 7]])
print("Problem B5", E.rref())

# Problem B6
F = sp.Matrix([[1, 1, 1, 1, 1, 5],
               [2, 3, 4, 5, 6, 20],
               [1, 0, 1, 0, 1, 3],
               [0, 1, 0, 1, 0, 2],
               [1, 2, 3, 4, 5, 15]])
print("Problem B6", F.rref())

# Problem B7
matrix_a = sp.Matrix([[1, 1, 1, 3],
                     [2, 3, 1, 7],
                     [-1, 1, 2, 2]])
print("Problem B7-a", matrix_a.rref())

matrix_b = sp.Matrix([[1, 1, 1, 1],
                     [1, 1, 1, 2],
                     [2, 2, 2, 3]])
print("Problem B7-b", matrix_b.rref())  

matrix_c = sp.Matrix([[1, -1, 1, 0],
                     [2, -2, 2, 0],
                     [3, -3, 3, 0]])
print("Problem B7-c", matrix_c.rref())
