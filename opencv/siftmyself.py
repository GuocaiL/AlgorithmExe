import cv2

img=cv2.imread('photo/bdlibrary2.jpg',1)
cv2.imshow('start',img)

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

detector=cv2.xfeatures2d.SIFT_create()

kps,des=detector.detectAndCompute(gray,None)

img=cv2.drawKeypoints(img,kps,gray)

cv2.imshow('detector',img)

cv2.waitKey()
cv2.destroyAllWindows()