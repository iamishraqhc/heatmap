import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('M1M2IE.csv', delimiter=',', header=None, skiprows=1, names=['Monolayer1','Monolayer2','IE-RF'])
# df = pd.read_csv('test.csv', delimiter=',', header=None, skiprows=1, names=['Monolayer1','Monolayer2','IE-RF'])
# print(df)
monolayer1 = df['Monolayer1']
monolayer2 = df['Monolayer2']
ierf = df['IE-RF']
# print(ierf)

df2 = df.pivot("Monolayer1","Monolayer2","IE-RF")
ax = sns.heatmap(df2)
plt.show()

ierf.plot(kind='hist')
plt.show()
