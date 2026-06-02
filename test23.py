import numpy as np

range_array = np.arange(10)
print(range_array)

x = np.array([[1, 1], [2, 2]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis=0)
print(z)

mat1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
unit_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(np.dot(mat1, unit_matrix))
print(mat1.max(axis=0))

data1 = np.array([[1, 2, 3], [3, 4, 5]])
ones = np.array([[1, 1, 1], [1, 1, 1]])
print(data1 + ones)

data2 = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data2)
print(data2 + ones_row)
