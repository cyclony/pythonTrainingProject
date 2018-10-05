import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
#函数式编程，模拟matlab模式，使用包pyplot中的函数 subplot，hist，plot等函数来创建图像。
#subplot(nrows, ncols, index)
#正态分布图，使用numpy的正态分布数据生成函数
#normal(mu,sigma, sampleNO): mu决定正态分布的中心（相对哪个值的正态分布），
# sigma指正态分布的数学方差，意思是偏离中心的距离，图像上表达为胖瘦区别，sigma越小，距离中心越近，图形越瘦
#sampleNO指生成的数据量大小
numbers =np.random.normal(0,8, 10000)#大数据绘图，如无必要，不用生成list分配内存，效率会更高
fit_xvalues = np.linspace(numbers.min(), numbers.max())
fit_yvalues = st.norm(0,8).pdf(fit_xvalues)

plt.subplot(2,2,1) #绘制在两行两列的第一个子图上
plt.hist(numbers, bins=100, normed=True)
plt.plot(fit_xvalues, fit_yvalues, color='r', linestyle='--')

y = [2.3, 3.4, 1.2, 6.6, 7.0]
plt.subplot(2,2,2)#绘制在两行两列的第二个子图上
plt.pie(y)

#使用默认绘图模式绘制余弦函数和正弦函数
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Y1, Y2 = np.sin(X), np.cos(X)
plt.subplot(2,2,3)#绘制在两行两列的第三个子图上
plt.plot(X, Y1)

x = [x for x in range(1,6)]
#y = np.random.rand(6)
y = [np.random.randint(10) for x in range(5)]
plt.subplot(2,2,4)#绘制上两行两列的第四个子图上
plt.bar(x, y)

plt.show()

