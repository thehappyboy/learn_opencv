import cv2
import numpy as np

dog = cv2.imread("./dog.jpeg")

# # 上下左右翻转
# al_dog = cv2.flip(dog, -1)
# # 上下翻转
# ud_dog = cv2.flip(dog, 0)
# # 左右翻转
# lr_dog = cv2.flip(dog, 1)
#
# cv2.imshow("dog", np.hstack((dog, lr_dog, ud_dog, al_dog)))

dog_90 = cv2.rotate(dog, cv2.ROTATE_90_CLOCKWISE)
dog_180 = cv2.rotate(dog, cv2.ROTATE_180)
dog_270 = cv2.rotate(dog, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("90", dog_90)
cv2.imshow("180", dog_180)
cv2.imshow("270", dog_270)


cv2.waitKey(0)
cv2.destroyAllWindows()
