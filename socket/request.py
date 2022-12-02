import socket #导入socket 模块
c = socket.socket()  #创建socket对象
host = '127.0.0.1'  #设置本地主机
port = 8888 #设置端口号
c.connect((host,port))
mess = input('你将要对服务端做什么？').encode()
c.send(mess)
print('客户端收到啦'.format(c.recv(2048)))
c.close()