from PIL import Image
from pathlib import Path
import numpy as np

IMAGE_PATH_1 = Path("c:/dev/sesac-python/data/image.png")
IMAGE_PATH_2 = Path("c:/dev/sesac-python/data/image2.png")


img1 = Image.open(IMAGE_PATH_1)
img2 = Image.open(IMAGE_PATH_2)

img_array_1 = np.array(img1)
img_array_2 = np.array(img2)

# 가로 세로를 일치시킨다. (img2를 img1 크기로 리사이즈)
h, w = img_array_1.shape[:2]          # img1의 (높이, 너비)
img2_resized = img2.resize((w, h))    # PIL resize는 (너비, 높이) 순서
img_array_2 = np.array(img2_resized)

# RGB 값의 평균을 구해 저장한다.
# uint8(0~255) 오버플로우를 막으려고 잠깐 큰 자료형으로 계산
blended = ((img_array_1.astype(np.uint16) + img_array_2.astype(np.uint16)) // 2).astype(np.uint8)

result = Image.fromarray(blended)
result.show()
