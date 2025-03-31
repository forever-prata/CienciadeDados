import pandas as pd

#Ex1
df = pd.read_csv('Filmes.csv')
print(df)

#Ex2
df.info()
df.head(8)

#Ex3
nomes_filmes = df['nome']
print(nomes_filmes)

#Ex4
filmes_e_notas = df[['nome','nota_imdb']]
print(filmes_e_notas)

#Ex5
filmes_e_notas.head(10)

#Ex6
filmes_e_notas.head(-4)

#Ex7
df2 = pd.DataFrame([
  [1, 'Parafuso de 3 polegadas', 0.5, 0.75],
  [2, 'Prego de duas polegadas', 0.10, 0.25],
  [3, 'Martelo', 3.00, 5.50],
  [4, 'Chave de fenda', 2.50, 3.00]
],
  columns=['ID do produto', 'Produto', 'Custofabricação', 'preço']
)
df2

df2['Margem'] = df2.preço - df2.Custofabricação

#Ex8
df3 = pd.read_csv('olimpíadas.csv')
df3.info()

#Ex9
df3[(df3.pais == 'Brazil') & (df3.sexo == 'M') & (df3.ano >= 2012) & (df3.idade > 30)]

#Ex10
media_idade = df3[df3.pais == 'Brazil']['idade'].mean()
print(media_idade)

#Ex11
atleta_mais_velho = df3[df3.pais == 'Brazil'].nlargest(1, 'idade')[['nome_atleta', 'idade', 'ano']]
print(atleta_mais_velho)

#Ex12
atleta_mais_jovem = df3[(df3.pais == 'Brazil') & (df3.medalha == 'Gold')].nsmallest(1, 'idade')[['nome_atleta', 'ano', 'idade']]
print(atleta_mais_jovem)

#Ex13
generos = df['genero'].unique()

#Ex14
media_notas_por_ano = df.groupby('ano')['nota_imdb'].mean()
print(media_notas_por_ano)
