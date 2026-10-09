import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv')
print(df[['SepalLengthCm', 'PetalWidthCm']])    