import cv2
import numpy as np

#open file
infmg=cv2.imread("photo/LONG.jpg",1)
#show infmg
cv2.imshow('source',infmg)
#convert to hsv
infmg_hsv=cv2.cvtColor(infmg,cv2.COLOR_BGR2HSV)
#get image shape
rows,cols,channels=infmg.shape
#print image info
print(cols,rows)
#copy file
frame=infmg_hsv.copy()
#color transfer
for r in range(0,rows):
   for c in range(0,cols):
         if((frame[r,c,0]>100) and (frame[r,c,0]<110) and (frame[r,c,2]>46) and (frame[r,c,1]>120) ):#blue?
                frame[r,c,0]=frame[r,c,0]-50

out_img=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
cv2.imshow("later",out_img)

while 1:
 key = cv2.waitKey(1)
 if key>0:
   break
cv2.destroyAllWindows()
