import numpy as np

# Question A1
# Verify the determinants
D1 = np.array([[4, 2], [1, 3]])
D2 = np.array([[1, 0, 2], [0, 3, 1], [4, 0, 1]])

det_D1 = np.linalg.det(D1)
det_D2 = np.linalg.det(D2)
print(f"Determinant of D1: {det_D1}")
print(f"Determinant of D2: {det_D2}")

# Question A2
X = np.array([[4.50, -3.50, 0.00],
              [-3.50, 4.50, 0.00],
              [0.00, 0.00, 2.00]])
A = np.array([[2.50, -1.50, 0.00],
              [-1.50, 2.50, 0.00],
              [0.00, 0.00, 2.00]])
B = np.array([[1.00, 0.00, 0.00],
              [0.00, 3.00, -1.00],
              [0.00, -1.00, 3.00]])

# Find the eigenvalues and eigenvectors of each matrix
eig_X = np.linalg.eig(X)
eig_A = np.linalg.eig(A)
eig_B = np.linalg.eig(B)
print(f"Eigenvalues and Eigenvectors of X: {eig_X}")
print(f"Eigenvalues and Eigenvectors of A: {eig_A}")
print(f"Eigenvalues and Eigenvectors of B: {eig_B}")

# Show that you can reconstruct the matrix X
reconstructed_X = eig_X[1] @ np.diag(eig_X[0]) @ np.linalg.inv(eig_X[1])
print(f"Reconstructed X (using inverse): {reconstructed_X}")
reconstructed_X2 = eig_X[1] @ np.diag(eig_X[0]) @ eig_X[1].T
print(f"Reconstructed X (using transpose): {reconstructed_X2}")

# Calculate your love score for candidate A and B
love_matrix_A = eig_X[1].T @ eig_A[1]
love_score_A = np.sum(np.abs(love_matrix_A))
love_matrix_B = eig_X[1].T @ eig_B[1]
love_score_B = np.sum(np.abs(love_matrix_B))
print(f"Love score for candidate A: {love_score_A}")
print(f"Love score for candidate B: {love_score_B}")

# Simulate interaction with person B
# 200 interactions
B_current = B.copy()
for i in range(200):
    B_current = X @ B_current
    if i % 10 == 0:
        B_current = B_current / np.linalg.norm(B_current)
B_200 = B_current

eig_B_200 = np.linalg.eig(B_200)
love_matrix_B200 = eig_X[1].T @ eig_B_200[1]
love_score_B200 = np.sum(np.abs(love_matrix_B200))

# 2000 interactions
B_current = B.copy()
for i in range(2000):
    B_current = X @ B_current
    if i % 10 == 0:
        B_current = B_current / np.linalg.norm(B_current)
B_2000 = B_current

eig_B_2000 = np.linalg.eig(B_2000)
love_matrix_B2000 = eig_X[1].T @ eig_B_2000[1]
love_score_B2000 = np.sum(np.abs(love_matrix_B2000))

print(f"Love score after 200 interactions: {love_score_B200}")
print(f"Love score after 2000 interactions: {love_score_B2000}")
print(f"Did B become a perfect soulmate? {np.isclose(love_score_B2000, 3.0, atol=0.1)}")

# Problem B3
