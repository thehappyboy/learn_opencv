import cv2
import numpy as np

lena = cv2.imread("./lena.jpeg")

h, w, ch = lena.shape

# 1. 获取仿射变换矩阵
M1 = cv2.getRotationMatrix2D((w // 2, h // 2), 30, 1)

# 2. 进行仿射变换
dst = cv2.warpAffine(lena, M1, (w, h))

while True:
    cv2.imshow("demo", np.hstack((lena, dst)))

    if cv2.waitKey(20) == ord("q"):
        break

cv2.destroyAllWindows()
