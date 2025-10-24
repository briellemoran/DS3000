#!/usr/bin/env python
import numpy as np
from numpy.linalg import eig, eigh, norm
np.set_printoptions(suppress=True, precision=4)


def pretty_np_array(m, title=None, end_space=''):
	m = str(m)
	L1 = m.split('\n')
	L1_max_width = len(max(L1, key=len))
	if title is not None:
		t1 = str.center(title, L1_max_width)
		m = t1 + '\n' + m + end_space
	else: m = m + end_space
	print(m, '\n')

# Original matrix A and eigenvalue matrix Λ
A = np.array([
    [2, -2, 0, 0],
    [-2, 2, 0, 0],
    [0, 0, 2.5005, -2.4995],
    [0, 0, -2.4995, 2.5005]
])

# Eigen-decomposition (A should already be symmetric)
λ, V = eigh(A)  # `eigh` guarantees real symmetric output and orthonormal V

# 1 - Verify A = V Λ V^T
Λ = np.diag(λ)
A_reconstructed = V @ Λ @ V.T
print("Original reconstruction:", A_reconstructed)

# 2 - Is A = V Λ V^T able to reconstruct your matrix?
non_trivial_indices = np.where(λ > 1e-10)[0]
Λ̃ = np.diag(λ[non_trivial_indices])
Ṽ = V[:, non_trivial_indices]
A_reconstructed_unit = Ṽ @ Λ̃ @ Ṽ.T
print("Non-trivial reconstruction:", A_reconstructed_unit)

# 3 - Is A = V Λ V^T able to reconstruct your matrix?
core_indices = np.where(λ > 0.01)[0]
Λ̄ = np.diag(λ[core_indices])
V̄ = V[:, core_indices]
core_reconstruction = V̄ @ Λ̄ @ V̄.T
print("Core reconstruction:", core_reconstruction)