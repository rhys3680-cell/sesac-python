import numpy as np

nd1 = np.arange(12).reshape(3, 4)

print(nd1)
print(nd1 > 4)
print(nd1[nd1 > 4])
print(nd1[[True, False, False], :2])
print(nd1[[False, True, True]][:, [False, False, True, True]])
