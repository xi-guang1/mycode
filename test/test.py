import time

def digui(x):
    print(x)
    return digui(x+1)

while 1:
    print("\a")
    time.sleep(2)