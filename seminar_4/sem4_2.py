import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (1000, 400)) 
ax1 = fig.add_subplot(211) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(212)
ax3 = fig.add_subplot(213)

# сгенерируем данные для какой-нибудь гистограммы
values = np.random.normal(0, 10, 1000)
values2 = np.random.normal(0, 100, 10000)
values3 = np.random.normal(0, 1000, 10000)

ax1.set_title('first hist')
ax1.hist(values, 50)
ax1.grid() # делаем сетку на графике ax1



ax2.hist(values2, 40)
ax2.grid()
ax2.set_title('second gist')


ax3.set_title('3rd')
ax3.hist(values3, 80)
ax3.grid() 
ax3.legend() 

plt.show()