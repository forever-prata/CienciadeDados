import pandas as pd
import matplotlib.pyplot as plt

df_cereais = pd.read_csv("cereais.csv",index_col = 0)
#df_cereais.head()
#df_cereais.info()
#df_cereais.describe()
#df_cereais.isnull().sum()

colunas_numerica = df_cereais.select_dtypes(include=['float64','int64']).columns
for col in colunas_numerica:
    if df_cereais[col].isnull().sum() > 0:
        df_cereais[col].fillna(df_cereais[col].mean(),inplace=True)

#df_cereais.info()

colunas_categoricas = ['name','mfr','type','shelf']
for col in colunas_categoricas:
    df_cereais[col] = df_cereais[col].astype('category')

#df_cereais.info()

df_cereais.rename(columns={
    'name' : 'Nome',
    'mfr' : 'Fabricante',
    'type' : 'Tipo',
    'fiber' : 'Fibra',
    'rating' : 'Avaliacao',
    'shelf' : 'Prateleira',
    'vitamins' : 'Vitaminas',
    'coupons' : 'Cupons',
    'price' : 'Preco'
}, inplace = True)

#df_cereais.duplicated().sum()
#df_cereais[df_cereais.duplicated()]
df_cereais.drop_duplicates(inplace = True)

#df_cereais['Fabricante'].value_counts()
#df_cereais['Tipo'].value_counts()

#df_cereais.groupby('Fabricante')['Avaliacao'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,5))
df_cereais['Fabricante'].value_counts().plot(kind='bar')
plt.title('Quantidade de Produtos por Fabricante')
plt.xlabel('Fabricante')
plt.ylabel('Numero de Cereais')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df_cereais.groupby('Fabricante')['Avaliacao'].mean().sort_values().plot(kind='barh')
plt.title('Avaliacao Media por Fabricante')
plt.xlabel('Avaliacao Media')
plt.ylabel('Fabricantes')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df_cereais['Fibra'].hist(bins=10)
plt.title('Distibuicao de Teor de Fibra')
plt.xlabel('Gramas de Fibra')
plt.ylabel('Frequencia')
plt.tight_layout()
plt.show()