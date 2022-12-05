from random import randint # 用于模拟掷硬币
import matplotlib.pyplot as plt # 用于画图
import numpy as np # 没用，可以忽略
from tqdm import tqdm #用于实现进度条

cishu = int(input('请输入试验次数')) # 获取输入的试验次数
x = range(1,cishu + 1) # 记录下每个点的横坐标
y = [] # 用于记录每个点的纵坐标
up = 0 # 向上的次数

for i in tqdm(x):
    up += randint(0,1) # 若为1则正面向上
    y.append(up/i) # 添加此时正面向上的频率

plt.plot(x,y) # 连线
plt.axis([0,cishu,0,1]) # 设置坐标轴的长度
plt.show() #显示图像