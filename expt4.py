from scipy import linalg, integrate, stats
import numpy as np

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
solution = linalg.solve(A, b)

integral, error = integrate.quad(lambda x: x**2, 0, 1)

data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
std_dev = np.std(data)

print("Solution to linear equations Ax = b:", solution)
print("\nDefinite integral of x^2 from 0 to 1:", integral)
print("\nMean of the sample data:", mean)
print("Standard deviation of the sample data:", std_dev)
