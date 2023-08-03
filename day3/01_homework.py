import cv2


# 导入logo和dog图像
# 将logo的图像设置为100*50, 并提取出来(只保留图像部分,剩余部分为黑色)
def logo_extracted(logo, size):
    logo_resized = cv2.resize(logo, size)
    logo_gray = cv2.cvtColor(logo_resized, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(logo_gray, 240, 255, cv2.THRESH_BINARY_INV)

    logo = cv2.bitwise_and(logo_resized, logo_resized, mask=mask)
    cv2.imshow("logo", logo)
    return logo


# 设置roi,插入logo
def logo_insert(logo, img):
    # 获取原始图片的尺寸,在左上角插入logo
    img_height, img_width, _ = img.shape
    logo_height, logo_width, _ = logo.shape
    # print(img_width, img_height)
    # print(logo_width, logo_height)

    # 设置roi区域
    roi = img[10 : logo_height + 10, img_width - logo_width - 10 : img_width - 10]
    # cv2.imshow("roi", roi)

    # 从roi中剔除logo区域
    logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY_INV)
    tmp = cv2.bitwise_and(roi, roi, mask=mask)

    # 插入图像
    dst = cv2.add(tmp, logo)

    img[10 : logo_height + 10, img_width - logo_width - 10 : img_width - 10] = dst

    return img


# roi = dog[:50, 500:


def main():
    logo_path = input("Input the logo img path: ")

    target_path = input("Input the target img path: ")
    target_img = cv2.imread(target_path)
    logo_img = cv2.imread(logo_path)

    logo = logo_extracted(logo_img, (100, 50))
    edited_img = logo_insert(logo, target_img)

    cv2.imshow("img", edited_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
