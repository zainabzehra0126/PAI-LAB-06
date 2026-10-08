import numpy as np

A = np.array([
    [4, 7],
    [2, 5]
])

B = np.array([
    [3, 2],
    [6, 5]
])

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)

print("\nAddition")
print("Shapes:", A.shape, B.shape)
print(A + B)

print("\nSubtraction")
print("Shapes:", A.shape, B.shape)
print(A - B)

print("\nElement-wise Multiplication")
print("Shapes:", A.shape, B.shape)
print(A * B)

print("\nMatrix Multiplication")
print("Shapes:", A.shape, B.shape)
print(A @ B)

print("\nTranspose of A")
print("Shape:", A.shape)
print(A.T)

print("\nTranspose of B")
print("Shape:", B.shape)
print(B.T)

print("\nDeterminant of A")
print("Shape:", A.shape)
print(np.linalg.det(A))

print("\nDeterminant of B")
print("Shape:", B.shape)
print(np.linalg.det(B))

print("\nInverse of A")
print("Shape:", A.shape)
print(np.linalg.inv(A))

print("\nInverse of B")
print("Shape:", B.shape)
print(np.linalg.inv(B))