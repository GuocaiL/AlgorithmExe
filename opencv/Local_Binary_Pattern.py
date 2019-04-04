import cv2
import numpy as np

radius=3
n_points=8*radius
image=cv2.imread('photo/LocalBinary.jpg')
cv2.imshow('image',image)
rows,cols,channels=image.shape
grayimg=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
lbpmem = np.zeros((rows, cols), np.uint8)
tmp = np.zeros((8,), np.uint8)
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if (grayimg[i, j] < grayimg[i - 1, j - 1]):
            tmp[0] = 1
        else:
            tmp[0] = 0
        if (grayimg[i, j] < grayimg[i - 1, j ]):
            tmp[1] = 1
        else:
            tmp[1] = 0
        if (grayimg[i, j] < grayimg[i - 1, j + 1]):
            tmp[2] = 1
        else:
            tmp[2] = 0
        if (grayimg[i, j] < grayimg[i , j + 1]):
            tmp[3] = 1
        else:
            tmp[3] = 0
        if (grayimg[i, j] < grayimg[i + 1, j + 1]):
            tmp[4] = 1
        else:
            tmp[4] = 0
        if (grayimg[i, j] < grayimg[i + 1, j ]):
            tmp[5] = 1
        else:
            tmp[5] = 0
        if (grayimg[i, j] < grayimg[i + 1, j - 1]):
            tmp[6] = 1
        else:
            tmp[6] = 0
        if (grayimg[i, j] < grayimg[i , j - 1]):
            tmp[7] = 1
        else:
            tmp[7] = 0
        lbpmem[i, j] = tmp[0] * 128 + tmp[1] * 64 + tmp[2] * 32 + tmp[3] * 16 + tmp[4] * 8 + tmp[5] * 4 + tmp[6] * 2 + tmp[7]
cv2.imshow('texture',lbpmem)
cv2.waitKey()
