import cv2
import numpy as np

dog = cv2.imread("./dog.jpeg")

# cv2.resize(dog, dsize=(800, 800), interpolation=cv2.INTER_LINEAR)
#
# cv2.imshow("resize", dog)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def onchage(value):
    pass


# 创建窗口
cv2.namedWindow("resize", cv2.WINDOW_AUTOSIZE)
# cv2.resizeWindow("resize", 640, 480)

# 读取图片
img = cv2.imread("./dog.jpeg")

# 创建trackbar
cv2.createTrackbar("horizontal", "resize", 1, 10, onchage)
cv2.createTrackbar("vertical", "resize", 1, 10, onchage)

while True:
    h_ratio = cv2.getTrackbarPos("horizontal", "resize")
    v_ratio = cv2.getTrackbarPos("vertical", "resize")

    resized_img = cv2.resize(img, None, fx=h_ratio, fy=v_ratio)
    cv2.imshow("resize", resized_img)

    if cv2.waitKey(10) == ord("q"):
        break

cv2.destroyAllWindows()
