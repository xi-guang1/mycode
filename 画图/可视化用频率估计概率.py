from random import randint
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

x = range(1,int(input('请输入试验次数')) + 1)
y = []
up = 0

for i in tqdm(x):
    up += randint(0,1)
    y.append(up/i)

plt.plot(x,y)
plt.show()