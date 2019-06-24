import socket                    # 调用socket库
import os

HOST = "192.168.70.175"          # 定义服务器ip
PORT = 65432                      # 定义端口号
addr = (HOST,PORT)               # 由于使用socket进行连接，需要把ip和端口先转换为元组
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # 设定了网络连接方式，以及传输使用的协议
c.settimeout(None)
c.connect(addr) #连接服务器

def send_file():
    filepath = '考察材料1.txt'      # 输入要从上传的文件
    if os.path.isfile(filepath):
        size=os.stat(filepath).st_size
        c.send(str(size).encode('utf-8'))
        print('发送文件大小:',size)
        with open(filepath,"rb") as f:            # 以只读方式打开指定的文件
            file = f.read()                  # 以byte 的方式读取文件内容
            c.sendall(file)                      # 发送文件内容

def get_file():
    # data = c.recv(1024)                     # 指定接受数据大小
    # print("开始接收："+data.decode('gbk'))
    # c.send(bytes('start ',encoding='gbk'))
    size1=int(c.recv(1024).decode('utf-8'))
    print('客户端接收文件1的大小：',size1)
    with open("短语.xlsx","wb") as f:       # 打开本地文件，将接受到的数据写入本地指定的目录
        f.write(c.recv(size1))
    # c.send(bytes('end ',encoding='gbk'))
    # data1=c.recv(1024)
    # print("开始接收："+str(data1))
    # c.send(bytes('start ',encoding='gbk'))
    c.send('接收文件2'.encode('utf-8'))
    size2=int(c.recv(1024).decode('utf-8'))
    print('客户端接收文件2的大小：',size2)
    with open('中心词.xlsx','wb') as g:
        g.write(c.recv(size2))


def main():
    send_file()
    get_file()
    c.close()


if __name__  == "__main__":                      # 调用main()函数
    main()
