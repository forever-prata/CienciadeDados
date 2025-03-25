import pandas as pd

#Dataframe a partid de um dicionario
df1 = pd.DataFrame({
    'nome' : ['Carlos Silva', 'Ana Souza', 'Joao Pereira',],
    'endereco' : ['Rua das Flores, 123', 'Av. Brasil, 456', 'Rua da Paz, 789'],
    'idade' : [34,28,51]
})
#df1

df2 = pd.read_csv('iris.csv')
#df2.head(-5)
#df2.info()
#df2.describe(include = 'all')

df3 = pd.read_csv('olimpíadas.csv')
#df3
#df3.info()

cidades_sede = df3['cidade_sede']
#cidades_sede
cidades_sede2 = df3.cidade_sede.unique()
#cidades_sede2

novoDF = df3[['pais','esporte']]
#novoDF

#df3.iloc[0]
#df3.iloc[:5]
#df3.iloc[2:5]
#df3.iloc[-2:]
#df3[df3.ano > 2012]
#df3[(df3.pais == 'Brazil) & (df3.medalha == 'Gold') & (df3.ano >= 2004)]
medalhas_por_pais = df3.groupby('pais').medalha.count()
#medalhas_por_pais[:30]

df4 = df3[(df3.ano >= 2008)].groupby(['pais','sexo']).medalha.count()
#df4[:30]

df5 = pd.DataFrame([
    [1,'Parafuso de 3 Polegadas',0.5,0.75],
    [2,'Prego de duas Polegadas',0.10,0.25],
    [3,'Martelo',3.00,5.50],
    [4,'Chave de Fenda',2.5,3.00]
],
    columns=['ID do Produto','Descricao','Custo de Fabricacao','Preco']
)
#df5
df5['Quantidade'] = [100,150,50,35]
#df5
df5['Em Estoque'] = 'OK'
#df5
df5['Imposto sobre Vendas'] = df5.preco * 0.075
#df5