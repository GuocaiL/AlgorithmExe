import cv2
import numpy as np

inputImgfile = 'photo/bdlibrary2.jpg'
outputImgfile = 'photo/bdlibrary_sift2.jpg'
outputfeature = 'photo/bdlibrary_sift2.txt'

# feature number
featureSum = 0
img = cv2.imread(inputImgfile,1)
cv2.imshow("library", img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
detector = cv2.xfeatures2d.SIFT_create()
# key point
kps, des = detector.detectAndCompute(gray, None)
# drawing key points
img = cv2.drawKeypoints(gray, kps, img)
cv2.imwrite(outputImgfile, img)
# save key point

np.savetxt(outputfeature, des, fmt='%.2f')
featureSum += len(kps)
cv2.imshow('result', img)

print('kps:' + str(featureSum))

while 1:
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()