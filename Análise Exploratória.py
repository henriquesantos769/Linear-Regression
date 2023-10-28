import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

from scipy.stats import kurtosis
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
from statsmodels.graphics.gofplots import qqplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.diagnostic import het_breuschpagan, het_goldfeldquandt,het_white
from statsmodels.stats.diagnostic import linear_harvey_collier, linear_reset, spec_white
from statsmodels.stats.diagnostic import linear_rainbow
from statsmodels.graphics.regressionplots import plot_leverage_resid2
from yellowbrick.regressor import CooksDistance
from statsmodels.stats.outliers_influence import OLSInfluence, variance_inflation_factor
from sklearn.linear_model import LinearRegression


cerveja_Df = pd.read_csv('Consumo_cerveja_sem_tratamento.csv')

'''
Visualizar as primeiras linhas do df
Drop de NA e exibir os tipos de variáveis das colunas
Somar as NAS 
'''

print(cerveja_Df.isna().sum())
cerveja_Df_clean = cerveja_Df.dropna()

print(cerveja_Df.head())
print(cerveja_Df_clean.dtypes)

#Transformações dos tipos de variáveis de cada coluna

cerveja_Df_clean['Temperatura Media (C)'] = cerveja_Df_clean['Temperatura Media (C)'].astype(str).str.replace(',', '.').astype(float)
cerveja_Df_clean['Temperatura Minima (C)'] = cerveja_Df_clean['Temperatura Minima (C)'].astype(str).str.replace(',', '.').astype(float)
cerveja_Df_clean['Temperatura Maxima (C)'] = cerveja_Df_clean['Temperatura Maxima (C)'].astype(str).str.replace(',', '.').astype(float)
cerveja_Df_clean['Precipitacao (mm)'] = cerveja_Df_clean['Precipitacao (mm)'].astype(str).str.replace(',', '.').astype(float)
cerveja_Df_clean['Final de Semana'] = cerveja_Df_clean['Final de Semana'].astype(int)
cerveja_Df_clean['Consumo de cerveja (litros)'] = cerveja_Df_clean['Consumo de cerveja (litros)'].astype(int)

"""
Exibir os valores dos tipos de variáveis modificados. Correlação das variáveis, e tabela descritiva.
"""
print(cerveja_Df_clean.dtypes)
print(cerveja_Df_clean.corr())
print(cerveja_Df_clean.describe)

#Temperatura mérdia máxima e mínima gráfico de linhas
cerveja_Df_clean[['Temperatura Media (C)',
         'Temperatura Minima (C)',
         'Temperatura Maxima (C)']].plot(figsize=(15,7));
plt.title('Séries de temperaturas máximas, Médias e Mínimas', size=15);
plt.show()

#Gráfico de precipitação diária
cerveja_Df_clean['Precipitacao (mm)'].plot(figsize=(15,7))
plt.title('Precipitação em mm',size=15);