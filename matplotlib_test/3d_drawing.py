import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #这个据说是必要的，否则会有add_subplot的参数报错，虽然似乎import没有用

fig = plt.figure()
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.show()

fig = plt.figure(2)

X = [np.random.choice(10,10)]
Y = [np.random.choice(10,10)]
Z = [np.random.choice(10,10)]
ax =fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z, c='r', marker='o')
plt.show()
