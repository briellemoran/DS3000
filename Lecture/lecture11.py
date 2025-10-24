import numpy as np

# Use Python to verify the spectrum theory with all 3 eigenvectors
v1 = np.array([[0.74], [-0.49], [-.47]])
v2 = np.array([[-0.29], [-0.85], [-0.43]])
v3 = np.array([[0.61], [-0.18], [0.77]])

λ1 = 5
λ2 = 4
λ3 = 0.0001

A = λ1 * (v1 @ v1.T) + λ2 * (v2 @ v2.T)
print(A)

B = λ1 * (v1 @ v1.T) + λ2 * (v2 @ v2.T) + λ3 * (v3 @ v3.T)
print(B)
