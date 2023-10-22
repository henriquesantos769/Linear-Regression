import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing


df = pd.read_csv("Real-estate1.csv")
print(df.head(5))
print(df.columns)


x = df.drop('Y house price of unit area', axis = 1)
y = df['Y house price of unit area']

print(x)
print(y)

sns.scatterplot(x = 'X4 number of convenience stores',
                y = 'Y house price of unit area', data=df)
plt.show()