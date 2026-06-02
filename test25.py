import numpy as np

nd1 = np.arange(12).reshape(3, 4)

print(nd1.shape)
print(nd1)
print(np.mean(nd1))
print(np.mean(nd1, axis=0))
print(np.mean(nd1, axis=1))
print(np.median(nd1, axis=0))
print(np.median(nd1, axis=1))
