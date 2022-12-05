from random import randint
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

cishu = int(input('请输入试验次数'))
x = range(1,cishu + 1)
y = []
up = 0

for i in tqdm(x):
    up += randint(0,1)
    y.append(up/i)

plt.plot(x,y)
plt.axis([0,cishu,0,1])
plt.show()