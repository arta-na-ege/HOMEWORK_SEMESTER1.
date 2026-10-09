import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sem4(25.09.2026)\BTC_data.csv')

time = list(df['time'])
prices = list(df['close'])

x = list(range(len(time)))

z = np.polyfit(x, prices, 3)
p = np.poly1d(z)

y_poly = []
for xi in x:
    y_poly.append(p(xi))

p = list(range(0, len(time), 100))
labels = [time[i] for i in p]

plt.plot(x, prices, label='цена')
plt.plot(x, y_poly, 'r', label='полином')
plt.xticks(p, labels)
plt.legend()
plt.show()