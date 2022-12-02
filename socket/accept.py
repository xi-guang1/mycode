import socket as sk

s = sk.socket()
host = "127.0.0.1"
port = 8888
s.bind((host,port))
s.listen(6)

while 1:
    conn,addr = s.accept()
    while 1:
        date = conn.recv(2048)
        if date:
            print("服务端收到，我再给你发一个包".format(date.decode()))
            conn.send(date)
        else:
            conn.close()#关闭连接
            break