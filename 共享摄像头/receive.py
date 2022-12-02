# import matplotlib.pyplot as plt
import base64
import socket as sk

s = sk.socket()
host = "192.168.0.124"
port = 8888
s.bind((host,port))
s.listen(6)

conn,addr = s.accept()
while 1:
    date = conn.recv(2048)
    if date:
        # img = date
        # print(img)
        # with open("共享摄像头\img\cs.png","wb") as f:
            # f.write(img)
        print(date.decode(encoding="utf-8"))