from PIL import Image
from pathlib import Path

import numpy as np


def rotate90_ccw(img_array: np.array):
    """반시계 90도 회전"""
    h, w = img_array.shape[:2]

    out = np.zeros((w, h) + img_array.shape[2:], dtype=img_array.dtype)
    for y in range(h):
        for x in range(w):
            new_x = y
            new_y = w - 1 - x
            out[new_y, new_x] = img_array[y, x]
    return out


IMAGE_PATH = Path("c:/dev/sesac-python/data/image.png")

img = Image.open(IMAGE_PATH)

img_array = np.array(img)

rotated = rotate90_ccw(img_array)

# 배열을 다시 이미지로 변환해서 화면에 띄우기
result = Image.fromarray(rotated)
result.show()

print(f"{img_array.shape} -> {rotated.shape}")
