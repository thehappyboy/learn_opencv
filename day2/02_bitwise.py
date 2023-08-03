import cv2
import numpy as np

cat = cv2.imread("./cat.jpeg")
dog = cv2.imread("./dog.jpeg")

# # bitwise_not
# cat_not = cv2.bitwise_not(cat)
# cv2.imshow("not", np.hstack((cat, cat_not)))
# print(cat[:3, :3])
# print(cat_not[:3, :3])

# # bitwise_and
# # cat - (316, 474, 3)
# # dog - (477, 600, 3)
# new_dog = dog[:316, :474]
#
# cat_and_dog = cv2.bitwise_and(new_dog, cat)
# cv2.imshow("and", np.hstack((cat, new_dog, cat_and_dog)))

# # bitwise or
# new_dog = dog[:316, :474]
#
# cat_or_dog = cv2.bitwise_or(new_dog, cat)
# cv2.imshow("or", np.hstack((new_dog, cat, cat_or_dog)))

# bitwise xor
new_dog = dog[:316, :474]
cat_xor_dog = cv2.bitwise_xor(new_dog, cat)
cv2.imshow("xor", np.hstack((new_dog, cat, cat_xor_dog)))


cv2.waitKey(0)
cv2.destroyAllWindows()
