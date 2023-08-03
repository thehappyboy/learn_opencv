import cv2
import numpy as np

img1 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img2 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)

print("img1: ")
print(img1)
print("img2: ")
print(img2)

# img1+img2, 用结果为对应元素累加后对256取模
print("img1+img2: ")
print(img1 + img2)

# cv2.add(img1, img2), 结果大于255时,结果为255
print("cv2.add(img1, img2)")
print(cv2.add(img1, img2))
