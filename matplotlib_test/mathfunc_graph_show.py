import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


#y=x^2 函数图像
X = np.arange(-256,256,1)
Y = X**2

ax1.set_title('x^2 function graph demo')
ax1.plot(X,Y)
ax1.grid(True) #添加网格线

#log 函数图像
Y = np.log(X)
ax2.plot(X,Y)
ax2.grid(True)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('log function graph')

X = np.linspace(-np.pi, np.pi, 256)
Y = np.sin(X)
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data',0))
ax3.spines['left'].set_position(('data',0))
ax3.set_title("sine funcion graph demo")
ax3.grid(True)
ax3.plot(X, Y,color='r', linestyle='--')

X = np.linspace(-np.pi, np.pi)
Y = np.cos(X)
ax4.set_title('cosine funcion graph demo')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
ax4.spines['bottom'].set_position(('data',0))
ax4.spines['left'].set_position(('data',0))
ax4.grid(True)
ax4.plot(X, Y)

plt.tight_layout() #自动调整子图之间间距以防止标题，标签之类相互重叠
plt.show()