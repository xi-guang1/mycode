# import matplotlib.pyplot as plt
import base64
import socket as sk

s = sk.socket()
host = '127.0.0.1'
port = 10809
s.bind((host,port))
s.listen(6)

client,addr = s.accept()


def receive_file(client):
    filename = client.recv(2048)
    if filename:
        with open(filename, 'wb') as f:
            while True:
                # 接收客户端传来的数据
                data = client.recv(1024)
                if not data:
                    break
                # 写入文件
                f.write(data)
    
    
    
while 1:
    date = client.recv(2048)
    if date:
        # img = date
        # print(img)
        # with open("共享摄像头\img\cs.png","wb") as f:
            # f.write(img)
        print(date.decode("utf-8"))