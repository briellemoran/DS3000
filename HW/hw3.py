import numpy as np
from space import space, point_cloud

# Homework 3, Verified Answers in Python

# Problem A1, d
P = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [-1, 0, 0]])

# Rotation matrix
Rz = np.array([[0, -1, 0],
               [1, 0, 0],
               [0, 0, 1]])

# Scaling matrix
S = np.array([[2, 0, 0],
              [0, 2, 0],
              [0, 0, 2]])

# Calculate final transformed points (from parts a, b, c)
P_final = P @ Rz @ S
app = space()
cloud = point_cloud(X=P)

# Define transformation function
def apply_transformation():
    cloud.redraw(P_final)
    print("Transformation applied!")
    print("Final points:")
    print(P_final)

app.accept('m', apply_transformation)

app.run()



# Problem B3, c
B3_i = np.array([[2, 3],
                 [1, 2]])

B3_ii = np.array([[1, 2, 3],
                  [0, 1, 4],
                  [2, 1, 0]])

B3_iii = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [0, 0, 0]])

B3_iv = np.array([[1, 2, 1, 0],
                  [0, 1, 4, 1],
                  [0, 0, 1, 3],
                  [0, 0, 0, 1]])
# Compute the inverse for each matrix
print("Problem B3-i:", np.linalg.inv(B3_i))
print("Problem B3-ii:", np.linalg.inv(B3_ii))
# print("Problem B3-iii:", np.linalg.inv(B3_iii))
# B3_iii is singular and does not have an inverse
print("Problem B3-iv:", np.linalg.inv(B3_iv))


# Problem B6, e
B6A = np.array([[2, 3, 4],
                [0, -1, 5],
                [0, 0, 3]])

B6B = np.array([[-1, 0, 0],
                [2, 4, 0],
                [1, -3, 2]])

B6C = np.array([[-2, 0, 0],
                [2, 0, 4],
                [1, -3, -3]])

# Compute |A|, |B|, |C|
print("|A|:", np.linalg.det(B6A))
print("|B|:", np.linalg.det(B6B))
print("|C|:", np.linalg.det(B6C))   

# Compute |2B|
print("|2B|:", np.linalg.det(B6B) * 2) 

# Compute |2BA^T|
print("|2BA^T|:", np.linalg.det(2 * B6B @ B6A.T))

# Compute |ABC|
print("|ABC|:", np.linalg.det(B6A @ B6B @ B6C))


# Problem B7, b
A_inv = np.linalg.inv(B6A)
B_T = B6B.T
M = A_inv @ B_T @ B6C @ B6A

# Caculate the determinant of M
det_M = np.linalg.det(M)
print("Problem B7:", det_M)
