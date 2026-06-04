import numpy as np

pt = np.array([2, 3])
ps = np.array([[2, 5], [5, 6], [6, 7]])

print(pt)
print(ps)

print(((ps - pt) ** 2).sum(1) ** 0.5**0.5)
