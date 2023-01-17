# from random import randint
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

point_num = 10000
x = np.random.uniform(-1,1,point_num)
y = np.random.uniform(-1,1,point_num)

# 画正方形
fig = plt.figure()
ax = fig.add_subplot(111)
rect = plt.Rectangle((-1, -1), 2, 2, fill=None)
ax.add_patch(rect)

# 画圆
circle = plt.Circle((0, 0), 1, fill=False)
ax.add_patch(circle)

plt.scatter(x, y, 1)
plt.axis('scaled')

distances = np.sqrt(x**2 + y**2)
in_circle_num = np.sum(distances < 1)
# print(in_circle_num)
# plt.legend(['1','2'],[f"总点数：{point_num}",f"在圆内的点数：{in_circle_num}"])
plt.show()

