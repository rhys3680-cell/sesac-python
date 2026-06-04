import numpy as np

ndArr1 = np.array([[[1, 2, 3]]])
ndArr1.sum()

# 4차원 배열 만들기 (shape: 2 x 3 x 4 x 5)
ndArr2 = np.arange(2 * 3 * 4 * 5).reshape(2, 3, 4, 5)

print(ndArr2)
print("ndim:", ndArr2.ndim)  # 차원 수 → 4
print("shape:", ndArr2.shape)  # 형태 → (2, 3, 4, 5)
print("size:", ndArr2.size)  # 전체 원소 개수 → 120
print("dtype:", ndArr2.dtype)  # 자료형

print(ndArr2.sum(axis=3))
