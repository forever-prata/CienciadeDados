import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

transacoes = pd.read_csv('Transacoes.csv')
#transacoes.head()
#transacoes.info()
#transacoes['fraude'].value_counts(normalize=True) * 100
amostra_fraude = transacoes[transacoes['fraude'] == 1]
amostra_nao_fraude = transacoes[transacoes['fraude'] == 0].sample(n=len(amostra_fraude),random_state=42)

df_visualizacao = pd.concat([amostra_fraude,amostra_nao_fraude])

#sns.boxplot(data=df_visualizacao,x='tipo',y='valor',hue='fraude')
#plt.title('Distribuição de Valores por por tipo de transação')
#plt.show()

transacoes = pd.get_dummies(transacoes,columns=['tipo'],prefix='tipo',dtype='int')

#transacoes.head()

transacoes['diferencaContas'] = (transacoes['saldoAnteriorOrigem'] - transacoes['saldoAnteriorDestino']).abs()

x = transacoes[['valor','saldoAnteriorOrigem','saldoAtualOrigem','saldoAnteriorDestino','saldoAtualDestino','diferencaContas','tipo_CASH_IN','tipo_CASH_OUT','tipo_DEBIT','tipo_PAYMENT','tipo_TRANSFER']]
y = transacoes[['fraude']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, stratify=y, random_state=42)

scaler = StandardScaler()
x_train_scalled = scaler.fit_transform(x_train)
x_test_scalled = scaler.transform(x_test)

modelos = {
    'Regressão Logística': LogisticRegression(),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(probability=True,random_state=42),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB()
}

resultados = []

for nome,modelo in modelos.items():
  if nome in ['SVM','KNN']:
    modelo.fit(x_train_scalled,y_train)
    y_prev = modelo.predict(x_test_scalled)
  else:
    modelo.fit(x_train,y_train)
    y_prev = modelo.predict(x_test)
  
  resultados.append({
      'Modelo': nome,
      'Acurácia': accuracy_score(y_test,y_prev),
      'Precisão': precision_score(y_test,y_prev,zero_division=0),
      'Recall': recall_score(y_test,y_prev),
      'F1-Score': f1_score(y_test,y_prev)
  })

df_resultados = pd.DataFrame(resultados)
df_resultados['Score_Combinado'] = (
    0 * df_resultados['Acurácia'] +
    0.25 * df_resultados['Precisão'] +
    0.5 * df_resultados['Recall'] +
    0.25 * df_resultados['F1-Score'] )

df_resultados_ordenado = df_resultados.sort_values(by='Score_Combinado',ascending=False).reset_index(drop=True)
df_resultados_ordenado