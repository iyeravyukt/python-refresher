import numpy as np

# Create a vector
a = np.array([1, 2, 3])
print(f"Vector a: {a}")

# Create a matrix
A = np.array([[1, 2], [3, 4]])
print(f"Matrix A: {A}")

# Create vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition of vectors
sum_vector = a + b
print(f"Sum of vectors a and b: {sum_vector}")

# Subtraction of vectors
diff_vector = a - b
print(f"Difference of vectors a and b: {diff_vector}")

# Dot product of vectors
dot_product = np.dot(a, b)
print(f"Dot product of vectors a and b: {dot_product}")

# Addition of matrices
sum_matrix = A + B
print(f"Sum of matrices A and B: {sum_matrix}")

# Subtraction of matrices
diff_matrix = A - B
print(f"Difference of matrices A and B: {diff_matrix}")

# Scalar multiplication of vectors
c = 2
scalar_mult_vector = c * a
print(f"Scalar multiplication of vector a by {c}: {scalar_mult_vector}")

# Scalar multiplication of matrices
scalar_mult_matrix = c * A
print(f"Scalar multiplication of matrix A by {c}: {scalar_mult_matrix}")

# Matrix multiplication
product_matrix = np.dot(A, B)
print(f"Product of matrices A and B: {product_matrix}")

# Transpose of a matrix
transpose_matrix = A.T
print(f"Transpose of matrix A: {transpose_matrix}")

import numpy as np

# Create a vector
a = np.array([1, 2, 3])

# Calculate the magnitude of the vector
magnitude = np.linalg.norm(a)
print(f"Magnitude of vector a: {magnitude}")

