import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sem4(25.09.2026)\BTC_data.csv')

time = pd.to_datetime(df['time']).dt.strftime('%d-%m-%y')
prices = list(df['close'])

x = list(range(len(time)))
s = 180

plt.plot(x, prices)
plt.xticks(x[::s], time[::s], rotation = 50)
plt.show()
 
