import numpy as np

# Verify if the eigenvectors Spans the basis
VT = np.array([[1, 2, 0],
               [2, 1, 0],
               [0, 0, 1]])
UT = np.array([[-0.707, 0, 0.707],
              [0.707, 0, 0.707],
              [0.000, 1, 0.000]])


left_side = UT.dot(UT.dot(VT))
right_side = VT.T
print(f"Left side: {left_side}")
print(f"Right side: {right_side}")


# Compute A^3
A = np.array([[4, 1, 1],
              [1, 3, 0],
              [1, 0, 3]])

rep_matrix_multiplication = A @ A @ A
matrix_power = np.linalg.matrix_power(A, 3)

print(f"A^3 using matrix multiplication:\n{rep_matrix_multiplication}")
print(f"A^3 using power:\n{matrix_power}")

eigenvalues, V = np.linalg.eig(A)
V_inverse = np.linalg.inv(V)
Λ = np.diag(eigenvalues)
Λ_3 = np.linalg.matrix_power(Λ, 3)
left_side = V @ Λ_3 @ V_inverse
print(f"Reconstructed A from eigen decomposition:\n{left_side}")