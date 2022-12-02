import matplotlib.pyplot as plt
import random
import numpy as np

x = np.array(random.randint(0,100) for i in range(10000))
y = np.array(random.randint(0,100) for i in range(10000))

plt.plot(x,y)
plt.show()
