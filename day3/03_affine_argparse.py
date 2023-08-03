import argparse
import cv2 as cv
import numpy as np

parser = argparse.ArgumentParser(description="Code for Affine Transformation tutorial.jlkasjdfklasdjlkafjakfjjsdkk")
parser.add_argument("--input", metavar="", help="Path to input image.", default="lena.jpeg")
args = parser.parse_args()

# 1. 读入图片
src = None
try:
    src = cv.imread(cv.samples.findFile(args.input, silentMode=True))
except Exception:
    print("Could not open or find image: ", args.input)
    exit(0)

# 2. 计算转换矩阵
src_tri = np.array([[0, 0], [src.shape[1] - 1, 0], [0, src.shape[0] - 1]]).astype(np.float32)
dst_tri = np.array(
    [
        [0, src.shape[1] * 0.33],
        [src.shape[1] * 0.85, src.shape[0] * 0.25],
        [src.shape[1] * 0.15, src.shape[0] * 0.7],
    ]
).astype(np.float32)

warp_mat = cv.getAffineTransform(src_tri, dst_tri)

warp_dst = cv.warpAffine(src, warp_mat, (src.shape[1], src.shape[0]))

# 3. 旋转图片
center = (warp_dst.shape[1] // 2, warp_dst.shape[0] // 2)
angle = -50
scale = 0.6

rot_mat = cv.getRotationMatrix2D(center, angle, scale)
rot_dst = cv.warpAffine(warp_dst, rot_mat, (src.shape[1], src.shape[0]))

cv.imshow("demo", np.hstack((src, warp_dst, rot_dst)))
cv.waitKey(0)
cv.destroyAllWindows()
