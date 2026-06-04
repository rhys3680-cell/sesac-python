import numpy as np

names = np.array(["김", "이", "정"])
scores = np.array([[90, 80, 70], [70, 80, 90], [100, 70, 70]])
ratio = np.array([0.5, 0.3, 0.2])
rank = np.argsort((scores * ratio).sum(1))[::-1][:2]

print(rank)
print(names[rank])
