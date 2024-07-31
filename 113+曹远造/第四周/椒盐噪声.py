import cv2
import random

img = cv2.imread('lenna.png', 0)
w, h = img.shape[:2]
s = 0.4
num = int(w*h*s)
for i in range(num):
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)
    if random.random() > 0.5:
        img[x,y] = 255
    else:
        img[x,y] = 0

cv2.imshow('椒盐噪声',img)
cv2.waitKey(0)
