import numpy as np

pt = np.array([2, 3])
ps = np.array([[2, 5], [5, 6], [6, 7]])


def distance(pt: np.ndarray, ps: np.ndarray):
    dst = (((ps - pt) ** 2).sum(1)) ** 0.5
    sp = np.argmin(dst)

    return ps[sp], dst[sp]


print(distance(pt, ps))
