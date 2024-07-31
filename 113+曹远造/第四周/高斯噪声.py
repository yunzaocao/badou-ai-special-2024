import cv2
import random
img = cv2.imread('lenna.png',0)
s = 0.2
w, h = img.shape[:2]
num = int(w * h * s)
for i in range(num):
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)
    newImg = img[x, y] + random.gauss(2, 4)
    if newImg > 255:
        img[x, y] = 255
    elif newImg < 0:
        img[x, y] = 0
cv2.imshow('高斯噪声:', img)
cv2.waitKey(0)


# 直接调用
from skimage import util
img1 = cv2.imread('lenna.png')
show = util.random_noise(img1, mode='gaussian')
cv2.imshow('直接调用:', show)
cv2.waitKey(0)
