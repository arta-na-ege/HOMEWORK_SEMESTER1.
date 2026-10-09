import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sem4(25.09.2026)/iris_data.csv')

cols = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

fig = plt.figure(figsize = (12, 10))

n = 1

for i in range(len(cols)):
    for j in range(i+1, len(cols)):
        ax = fig.add_subplot(2, 3, n)

        x = df[cols[i]]
        y = df[cols[j]]

        ax.scatter(x, y,)

        # мнк
        k, b = np.polyfit(x, y, 1)
        x_ln = np.linspace(x.min(), x.max(), 150)
        ax.plot(x_ln, k*x + b, color= 'green')

        ax.set_xlabel(cols[i])
        ax.set_ylabel(cols[j])
        ax.grid()

        n+=1

plt.tight_layout()
plt.show()