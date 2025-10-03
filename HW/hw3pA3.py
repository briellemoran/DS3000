import numpy as np
from space import space, point_cloud

# Define the original 3D object
P = np.array([[3, 1, 2],
              [5, 1, 2],
              [5, 4, 2],
              [3, 4, 2],
              [3, 1, 5],
              [5, 1, 5],
              [5, 4, 5],
              [3, 4, 5]])

# Calculate the mean (centroid) of the object
mean = np.mean(P, axis=0)

# Create centering matrix
n = P.shape[0]
I = np.eye(n)
ones = np.ones((n, 1))
H = I - (1/n) * (ones @ ones.T)

# Center the object
P_centered = H @ P

# Create the 3D visualization
app = space()

# Create initial point cloud
cloud = point_cloud(X=P)

# Store current state
current_points = P.copy()

# Rotation matrices (15 degree increments)
angle = np.radians(15)

Rx = np.array([[1, 0, 0],
               [0, np.cos(angle), -np.sin(angle)],
               [0, np.sin(angle), np.cos(angle)]])

Ry = np.array([[np.cos(angle), 0, np.sin(angle)],
               [0, 1, 0],
               [-np.sin(angle), 0, np.cos(angle)]])

Rz = np.array([[np.cos(angle), -np.sin(angle), 0],
               [np.sin(angle), np.cos(angle), 0],
               [0, 0, 1]])

# Scaling matrices
scale_up = np.eye(3) * 1.1
scale_down = np.eye(3) * 0.9

def apply_transformation(transform_matrix):
    global current_points
    
    # Center the object (move to origin)
    centered = current_points - mean
    
    # Apply transformation
    transformed = centered @ transform_matrix
    
    # Move back to original position
    final = transformed + mean
    
    current_points = final
    cloud.redraw(final)

# Key bindings for rotations
def rotate_x():
    apply_transformation(Rx)
    print("Rotated around X-axis")

def rotate_y():
    apply_transformation(Ry)
    print("Rotated around Y-axis")

def rotate_z():
    apply_transformation(Rz)
    print("Rotated around Z-axis")

# Key bindings for scaling
def scale_smaller():
    apply_transformation(scale_down)
    print("Scaled smaller")

def scale_bigger():
    apply_transformation(scale_up)
    print("Scaled bigger")

# Bind keys
app.accept('x', rotate_x)
app.accept('y', rotate_y)
app.accept('z', rotate_z)
app.accept('s', scale_smaller)
app.accept('b', scale_bigger)

# Print instructions
print("Controls:")
print("  x - Rotate around X-axis")
print("  y - Rotate around Y-axis")
print("  z - Rotate around Z-axis")
print("  s - Scale smaller")
print("  b - Scale bigger (b for Bigger)")
print("\nDrag mouse to rotate view, scroll to zoom")

app.run()