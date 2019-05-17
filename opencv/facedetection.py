"""
import cv2

filename='pic1.jpg'

def detect(filename):
   face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
   img = cv2.imread(filename)
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.02, 5)
   for (x,y,w,h) in faces:
         img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   cv2.namedWindow('person Detected!!')
   cv2.imshow('person Detected!!', img)
   cv2.imwrite('person.jpg', img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

detect(filename)
"""
import cv2

def detect():
   face_cascade = cv2.CascadeClassifier('xmlfile/haarcascade_frontalface_default.xml')
   eye_cascade=cv2.CascadeClassifier('xmlfile/haarcascade_eye.xml')
   camera=cv2.VideoCapture(0)
   while(True):
      ret, img=camera.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.02, 5)
      for (x,y,w,h) in faces:
         img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray=gray[y:y+h,x:x+w]
         eyes=eye_cascade.detectMultiScale(roi_gray,1.01,5, 0, (40,40))
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+ey),(0,255,0),2)
         cv2.imshow("camera",img)
         if(cv2.waitKey(1000//12)&0xff==ord("q")):
              break;
   camera.release()
   cv2.destroyAllWindows()

detect()
