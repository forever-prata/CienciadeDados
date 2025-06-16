from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Regressão Linear Simples
temperaturas = np.array(range(0,40,2))
temperaturas = temperaturas.reshape(-1,1)
vendas = [65,58,46,45,44,42,40,40,36,38,38,28,30,22,27,25,25,20,15,5]

#plt.plot(temperaturas,vendas,'o')
#plt.ylabel('Vendas')
#plt.xlabel('Temperatura')
#plt.show()

interceptacao = 65
inclinacao = -2

#plt.plot(temperaturas,vendas,'o')
#plt.ylabel('Vendas')
#plt.xlabel('Temperatura')
#y = [interceptacao + inclinacao * x for x in temperaturas]
#plt.plot(temperaturas,y)
#plt.show()

#erro = 0
#for i,j in zip(y,vendas):
    #erro += (i-j)**2
#print(erro)

regressaoLinear = LinearRegression()
regressaoLinear.fit(temperaturas,vendas)

previsao_vendas = regressaoLinear.predict(temperaturas)
#plt.plot(temperaturas,vendas,'o')
#plt.ylabel('Vendas')
#plt.xlabel('Temperatura')
#plt.plot(temperaturas,previsao_vendas)
#plt.show()

#regressaoLinear.coef_
#regressaoLinear.intercept_
#regressaoLinear.predict([[19]])
#r2_score(vendas,previsao_vendas)

moradias = pd.read_csv('moradias.csv')

x = moradias[['bedrooms','bathrooms','size_sqft','min_to_subway','floor','building_age_yrs']]
moradias[['bedrooms','bathrooms','size_sqft']]
y = moradias[['rent']]

scaler = MinMaxScaler()
x_minmax = scaler.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_minmax,y,train_size=0.8)

#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)

regressaoMultipla = LinearRegression()
regressaoMultipla.fit(x_train,y_train)

previsao_y = regressaoMultipla.predict(x_test)

#plt.scatter(y_test,previsao_y)
#plt.xlabel('Valores Reais')
#plt.ylabel('Valores Previstos')
#plt.show()

r2_score(y_test,previsao_y)

#corr = moradias.corr(numeric_only=True)
#corr.style.background_gradient(cmap='coolwarm').format(precision=2)

rmse = np.sqrt(mean_squared_error(y_test,previsao_y))
#rmse

mae = mean_absolute_error(y_test,previsao_y)
#mae