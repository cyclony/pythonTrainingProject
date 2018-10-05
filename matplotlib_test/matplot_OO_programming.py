import matplotlib.figure as Figure
import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.normal(0, 2, 1000000)
numbers = [random.choice(range(1,10)) for x in range(10)]
mean = np.average(numbers)
names = list('abcdefghik')
fig, ax = plt.subplots()
plt.style.use('fivethirtyeight')
ax.barh(names, numbers)
line = ax.axvline(mean, ls='--', color='red')

plt.show()