import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing
import scipy.stats as stats

dados = pd.read_csv("dados.csv")
dados.drop('Altura', inplace = True, axis=1)

#Exibir as primeiras 5 linhas, e colunas do df.
print(dados.head(5))
print(dados.columns)

#Printar valores nulos e NA
print(dados.isnull().sum())
print(dados.isna().sum())

"""
Plotar um gráfico para visualizar a relação entre "Anos de Estudo", variavel Idependente,
e Renda, variavel dependente.
"""
sns.scatterplot(x = 'Anos de Estudo', y = 'Renda', data = dados)
plt.show()

X = dados.drop('Renda', axis=1)
y = dados['Renda']

print(X)
print(y)


# Criar o Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

"""
Inicializar o modelo, e filtra-lo.
"""
model = LinearRegression()
model.fit(X_train, y_train)

#Fazer predições
predictions = model.predict(X_test)

coefficients = model.coef_
print("Coeficientes:", coefficients)

r_squared = model.score(X, y)
print("Coeficiente de Determinação (R²):", r_squared)


print('mean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))

'''
Calcule os resíduos subtraindo as previsões do modelo dos valores reais da variável dependente.
'''

y_list = y.tolist()

# Calcular os resíduos usando as listas
residuos = [y_i - pred_i for y_i, pred_i in zip(y_list, predictions)]

"""
Crie um histograma dos resíduos para verificar se eles seguem uma distribuição normal.
"""

plt.hist(residuos, bins=30)
plt.xlabel('Resíduos')
plt.ylabel('Frequência')
plt.title('Histograma dos Resíduos')
plt.show()

"""
O gráfico QQ é usado para comparar a distribuição dos resíduos com uma 
distribuição normal. Se os pontos estiverem próximos a uma linha diagonal, 
isso sugere que os resíduos estão normalmente distribuídos.

"""
plt.scatter(predictions, residuos)
plt.xlabel('Valores Previstos')
plt.ylabel('Resíduos')
plt.axhline(y=0, color='r', linestyle='--')  # Linha de referência em y=0
plt.title('Gráfico de Dispersão dos Resíduos em Relação às Previsões')
plt.show()


residuos_ordenados = np.sort(residuos)
z_teoricos = stats.norm.ppf(np.linspace(0.001, 0.999, len(residuos)))
plt.scatter(z_teoricos, np.sort(residuos))
plt.xlabel('Quantis Teóricos (Distribuição Normal)')
plt.ylabel('Resíduos Ordenados')
plt.title('Gráfico QQ dos Resíduos')
plt.show()