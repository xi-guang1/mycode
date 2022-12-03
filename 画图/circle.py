import numpy as np
import matplotlib.pyplot as plt

r = 1
a,b = 0,0
theta = np.arange(0,2*np.pi,0.01)
x = a + r * np.cos(theta)
y = a + r * np.sin(theta)

plt.plot(x,y)
plt.show()
# print(x,y)