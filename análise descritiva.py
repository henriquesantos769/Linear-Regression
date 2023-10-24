import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

df = pd.read_csv('Real-estate1.csv')
print(df.info())
print(df.head())
print(df['Y house price of unit area'].describe())

# Histograma das variáveis
x = df.drop(['No','X1 transaction date', 'X5 latitude','X6 longitude'],axis=1)
x.hist(figsize=(12, 8))
plt.show()

# Box plot para Y house price of unit area
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Y house price of unit area'])
plt.title('Box Plot para Preço por Unidade de Área')
plt.ylabel('Preço por Unidade de Área')
plt.show()

# Gráfico de distribuição do preço das casas por unidade de área
plt.figure(figsize=(12, 6))
sns.histplot(df['Y house price of unit area'], kde=True)
plt.title('Distribuição do Preço das Casas por Unidade de Área')
plt.xlabel('Preço por Unidade de Área')
plt.ylabel('Frequência')
plt.show()

# lasso para a verificação dos atributos mais importantes
# Create X and y arrays
X = df.drop(["Y house price of unit area"], axis=1)
y = df["Y house price of unit area"].values
sales_columns = X.columns

# Instantiate a lasso regression model
lasso = Lasso(alpha=0.3)

# Compute and print the coefficients
lasso_coef = lasso.fit(X,y).coef_
print(lasso_coef)
plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()

# Scatter plot de idade da casa vs. preço
plt.figure(figsize=(12, 6))
sns.scatterplot(x='X2 house age', y='Y house price of unit area', data=df)
plt.title('Scatter Plot: Idade da Casa vs. Preço')
plt.show()

# Scatter plot de distância até o metrô vs. preço
plt.figure(figsize=(12, 6))
sns.scatterplot(x='X3 distance to the nearest MRT station', y='Y house price of unit area', data=df)
plt.title('Scatter Plot: Distância para a Estação MRT vs. Preço')
plt.show()

