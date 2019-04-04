import cv2
import numpy as np

#建立画布
img=np.zeros((500,500,3),np.uint8)
#利用polylines函数绘画正方体
pts=np.array([[50,100],[100,50],[200,50],[150,100],[50,100],[50,200],[150,200],[150,100],[200,50],[200,150],[150,200]],np.int32)
pts=pts.reshape(-1,1,2)
img=cv2.polylines(img,[pts],False,(0,255,255))

#贴图样本
total=np.zeros((200,200,3),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
total=cv2.putText(total,'liguocai',(10,56),font,0.7,(255,255,255),2,cv2.LINE_AA)
rows,cols,weight=total.shape

#将贴图样本贴到正方体正面
img[101:199,51:149]=total[1:99,1:99]

#将贴图样本贴到正方体上面
#变换
post1=np.float32([[0,0],[100,0],[0,100]])
post2=np.float32([[60,50],[160,50],[0,100]])
MUp=cv2.getAffineTransform(post1,post2)
imgUp=cv2.warpAffine(total,MUp,(cols,rows))
#渲染
for rowUp in range(51,100):
    for colUp in range(151-rowUp, 250-rowUp):
        img[rowUp,colUp]=imgUp[rowUp,colUp-45]

#将贴图样本贴到正方体侧面，分为两步，第一步将贴图样本旋转，第二步进行变换和渲染
#旋转
Mrotated=cv2.getRotationMatrix2D((100,100),-90,1.0)
rotated=cv2.warpAffine(total,Mrotated,(cols,rows))
#变换
post1=np.float32([[100,0],[199,0],[100,100]])
post2=np.float32([[150,50],[199,0],[150,150]])
MRight=cv2.getAffineTransform(post1,post2)
imgRight=cv2.warpAffine(rotated,MRight,(cols,rows))
#渲染
for colRight in range(151, 200):
    for rowRight in range(251-colRight,349-colRight):
         img[rowRight,colRight]=imgRight[rowRight-50,colRight]
         imgRight[rowRight - 50, colRight ]=(255,0,0)


cv2.imshow("second homework",img)
cv2.waitKey()
cv2.destroyAllWindows()


