import numpy as np

nd1 = np.arange(12).reshape(3, 4)

print(nd1.shape)
print(nd1)
print(nd1[1][2])
print(nd1[1:, :])
print(nd1[:, 1:2])
print(nd1[1:, 2:])
