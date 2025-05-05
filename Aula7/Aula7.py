import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr

estudantes = pd.read_csv('alunos.csv')
#estudantes.head()
#estudantes.info()

scores_urbano = estudantes.G3[estudantes.address == 'U']
scores_rural = estudantes.G3[estudantes.address == 'R']

media_aluno_urbano = np.mean(scores_urbano)
media_aluno_rural = np.mean(scores_rural)

print(f"Media dos alunos urbano: {media_aluno_urbano:.2f}")
print(f"Media dos alunos rural: {media_aluno_rural:.2f}")
print(f"Diferença média: {media_aluno_urbano - media_aluno_rural:.2f}")

#sns.boxplot(data = estudantes, x = 'address', y = 'G3')

plt.hist(scores_urbano, color="blue", label="Urbano", density=True, alpha =0.5)
plt.hist(scores_rural, color="red", label="Rural", density=True, alpha =0.5)
plt.xlabel("Pontuação")
#plt.legend()

#fig , axs = plt.subplots(1,2, figsize=(10,5))

#sns.boxplot(data = estudantes, x = 'Mjob', y = 'G3', ax = axs[0])
#axs[0].set_title("Boxplot Profissão Mãe")

#sns.boxplot(data = estudantes, x = 'Fjob', y = 'G3', ax = axs[1])
#axs[1].set_title("Boxplot Profissão Pai")

moradias = pd.read_csv('moradias.csv')

plt.scatter(x = moradias.size_sqft, y = moradias.rent)
plt.xlabel("Tamanho")
plt.ylabel("Aluguel")
plt.show()

plt.scatter(x = moradias.building_age_yrs, y = moradias.rent)
plt.xlabel("Idade")
plt.ylabel("Aluguel")
plt.show()

corr_aluguel_tamanho , p = pearsonr(moradias.rent, moradias.building_age_yrs)
print(f"Correlação Aluguel x Tamanho: {corr_aluguel_tamanho:.2f}")

corr = moradias.corr(numeric_only= True)
corr.style.background_gradient(cmap='coolwarm').format(precision=2)