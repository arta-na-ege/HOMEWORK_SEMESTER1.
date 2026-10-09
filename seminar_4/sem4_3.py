import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('sem4(25.09.2026)/iris_data.csv')

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

species_counts = df['Species'].value_counts()

ax1.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%')
ax1.set_title('Доля видов ирисок')


petal = df['PetalLengthCm']

less_12 = (petal < 1.2).sum()
from12_to_15 = ((petal >= 1.2) & (petal <= 1.5)).sum()
more_15 = (petal > 1.5).sum()

sizes = [less_12, from12_to_15, more_15]
label = ['меньше 12 мм', 'между 12 и 15 мм', 'больше 15 мм']

ax2.pie(sizes, labels= label, autopct='%1.1f%%',colors=['lightcoral', 'lightskyblue', 'lightgreen'])
ax2.set_title('селекция по длине лепестка')

# функцию на tight_layout() подсмотрел в дипсике
plt.tight_layout()
plt.show()