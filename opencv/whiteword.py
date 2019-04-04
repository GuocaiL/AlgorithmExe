import cv2
import numpy as np

#读取图片
source=cv2.imread('photo/color.jpg',1)
#显示图片
cv2.imshow('source',source)
#Creates an instance of GrayworldWB.
wb = cv2.xphoto.createGrayworldWB()
#Maximum saturation for a pixel to be included in the gray-world assumption.
wb.setSaturationThreshold(0.7)
#transfer
White = wb.balanceWhite(source)
cv2.imshow('white world',White)
cv2.waitKey()
cv2.destroyAllWindows()
