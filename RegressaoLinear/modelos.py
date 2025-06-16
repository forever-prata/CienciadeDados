from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

moradias = pd.read_csv('moradias.csv')

x = moradias[['bedrooms','bathrooms','size_sqft']]
y = moradias[['rent']]

scaller = MinMaxScaler()
x_minmax = scaller.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_minmax,y,train_size=0.8,random_state=42)

modelos = {
    'Regressão Linear': LinearRegression(),
    'Regressão Ridge': Ridge(),
    'Regressão Lasso': Lasso(),
    'Árvore de Decisão': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42, n_estimators=100),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42),
    'KNN': KNeighborsRegressor(n_neighbors=5)
}

resultados = []

for nome,modelo in modelos.items():
    modelo.fit(x_train,y_train)
    y_prev = modelo.predict(x_test)

    mae = mean_absolute_error(y_test,y_prev)
    rmse = np.sqrt(mean_squared_error(y_test,y_prev))
    r2 = r2_score(y_test,y_prev)

    resultados.append({
        'Modelo': nome,
        'MAE': mae,
        'RMSE': rmse,
        'R2': r2
    })

df_resultados = pd.DataFrame(resultados)
#df_resultados

df_resultados[['MAE_norm','RMSE_norm']] = scaller.fit_transform(df_resultados[['MAE','RMSE']])
df_resultados['R2_norm'] = scaller.fit_transform(df_resultados[['R2']])

df_resultados['Score_Combinado'] = (
    0.4 * (1 - df_resultados['MAE_norm']) +
    0.4 * (1 - df_resultados['RMSE_norm']) +
    0.2 * (1 - df_resultados['R2_norm'])
)

df_resultados_ordenado = df_resultados.sort_values(by='Score_Combinado',ascending=False).reset_index(drop=True)
#df_resultados_ordenado

df_resultados.set_index('Modelo')[['MAE','RMSE']].plot(kind='bar',figsize=(10,6))
plt.title('Comparação de Erros')
plt.ylabel('Erro')
plt.xticks(rotation=45)
plt.grid(True)

melhor_modelo_nome = df_resultados_ordenado.loc[0,'Modelo']
melhor_modelo = modelos[melhor_modelo_nome]
joblib.dump(melhor_modelo,f'melhor_modelo{melhor_modelo_nome}.pk1')

print(f'Melhor modelo: {melhor_modelo_nome} Salvo com sucesso')

modelo = joblib.load('melhor_modeloGradient Boosting.pk1')

novos_dados = pd.DataFrame({
    'bedrooms' : [2,3],
    'bathrooms' : [1,2],
    'size_sqft' : [700,1000]
})

previsoes = modelo.predict(novos_dados)

for i in range(len(novos_dados)):
  print(previsoes[i])