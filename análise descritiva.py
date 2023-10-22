import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Real-estate1.csv')
'''
print(df.head())
print(df.describe())
'''
# Histograma das variáveis
x = df.drop(['No'],axis=1)
x.hist(figsize=(12, 8))
plt.show()

# Matriz de correlação
correlacao = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Scatter plot de variáveis vs. preço
plt.figure(figsize=(12, 6))
sns.scatterplot(x='X2 house age', y='Y house price of unit area', data=df)
plt.title('Scatter Plot: Idade da Casa vs. Preço')
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='X3 distance to the nearest MRT station', y='Y house price of unit area', data=df)
plt.title('Scatter Plot: Distância para a Estação MRT vs. Preço')
plt.show()
