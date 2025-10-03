import numpy as np
from space import space, point_cloud

# Define the original points
X = np.array([[2, 3],
              [4, 5],
              [6, 7],
              [8, 9]])

X_3D = np.column_stack([X, np.zeros(4)])

# Construct the centering matrix
n = 4
I = np.eye(n)
ones = np.ones((n, 1))
H = I - (1/n) * (ones @ ones.T)

# Apply centering to get centered points
X_centered = H @ X

# Add z-coordinate to centered points for 3D visualization
X_centered_3D = np.column_stack([X_centered, np.zeros(4)])
app = space()

# Create initial point cloud with original points
cloud = point_cloud(X=X_3D)

# Define centering function
def apply_centering():
    cloud.redraw(X_centered_3D)
    print("Centering applied!")
    print("Original points:")
    print(X)
    print("\nCentered points:")
    print(X_centered)
    print("\nMean of centered points:")
    print(np.mean(X_centered, axis=0))

# Bind 'm' key to apply centering
app.accept('m', apply_centering)
app.run()