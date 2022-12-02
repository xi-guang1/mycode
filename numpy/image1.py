import numpy as np
from PIL import Image
from matplotlib import cm as mplcm

# img1 = np.random.randint(0,255,(100,300,3),dtype=np.uint8)
# img1 = Image.fromarray(img1)
# img1.show()

r = np.tile(np.linspace(192,255,300,dtype=np.uint8),(600,1)).T
g = np.tile(np.linspace(192,255,600,dtype=np.uint8),(300,1))
b = np.ones((300,600), dtype=np.uint8)*224
img1 = np.dstack((r,g,b))
Image.fromarray(img1,mode="RGB").show()
# print(img1)

r = np.tile(np.linspace(192,255,300,dtype=np.uint8),(600,1)).T
g = np.tile(np.linspace(192,255,600,dtype=np.uint8),(300,1))
b = np.ones((300,600), dtype=np.uint8)*224
im = np.dstack((r,g,b))
Image.fromarray(im, mode='RGB').show()
