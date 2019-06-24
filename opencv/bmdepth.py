import numpy as np
import cv2
#
#block_size = 5
mum_disp = 16

imgL = cv2.imread('photo\left1.jpg')
#cv2.imshow('left1',imgL)
imgLG= cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
imgR = cv2.imread('photo\\right1.jpg')
imgRG= cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
#cv2.imshow('right1',imgR)

stereo = cv2.StereoBM_create(numDisparities=mum_disp, blockSize=11)
disp = stereo.compute(imgLG, imgRG)
cv2.imshow('disparity', disp)
cv2.imwrite('depth_bm.jpg',disp)

cv2.waitKey()
	
cv2.destroyAllWindows()

