import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

addition = np.add(matrix_a, matrix_b)
elementwise_multiplication = np.multiply(matrix_a, matrix_b)
transpose_a = np.transpose(matrix_a)
determinant_a = np.linalg.det(matrix_a)

print("Matrix A + Matrix B:")
print(addition)
print("\nElement-wise Multiplication of Matrix A and Matrix B:")
print(elementwise_multiplication)
print("\nTranspose of Matrix A:")
print(transpose_a)
print("\nDeterminant of Matrix A:")
print(determinant_a)
