#coding=UTF-8
import cv2

#打开设备的摄像头，0代表设备标准的视频输入设备，如果打开其它的视频输入设备则替换为1
cap=cv2.VideoCapture(0)

#打印是否捕获成功
print(cap.isOpened())

while (1):
    #将捕捉到的内容读到img，若能读取成功则red为true，否则为false，读取成功后内容保存在img中
    ret,img=cap.read()
    #显示捕捉的内容
    cv2.imshow("1801220008",img)
    #调用键盘输入
    key=cv2.waitKey(1)
    #点击ESC键退出循环
    if key==27:
        break

#释放cap
cap.release()

#关闭窗口
cv2.destroyAllWindows()
