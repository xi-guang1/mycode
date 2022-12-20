import base64
import socket as sk #导入socket 模块
c = sk.socket()  #创建socket对象
host = 'xjp-1.muhanfrp.cn'  #设置本地主机
port = 10809 #设置端口号
c.connect((host,port))

def img_read(path):
    with open(path,'rb') as f:
        return f

def img_byte(path):
    with open(path,'rb') as f:
        res = base64.b64encode(f.read())
    return res

# print(img_byte("共享摄像头\img\zhangai.png"))
c.send('已发送')
print('客户端收到啦')
c.close()