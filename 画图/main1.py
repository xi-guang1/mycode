import numpy as np
import matplotlib.pyplot as plt

def fun(a = 0,b = 0,c = 0):
    a = float(input("请输入a"))
    b = float(input("请输入b"))
    c = float(input("请输入c"))
    x = np.linspace(-100,100,1000)
    y = a * x ** 2 + b * x + c
    plt.plot(x,y)
    plt.show()

fun()
