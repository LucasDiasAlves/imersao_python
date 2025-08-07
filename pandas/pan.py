import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

import plotly.io as pio
pio.renderers.default = 'browser'

# url para carregar a tabela csv e atribuindo p valor da url a variavel df(data frame) 
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)

# print(df.info()) -- para mostrar informações de tipos de gerais da tabela

# print(df.describe())-- para descrever melhor sobre a tabela, traz estatisticas descritivas, apenas variaveis numericas

# print(df.shape) -- traz a dimenção do arquivo, (linhas, colunas)

linhas, colunas = df.shape[0], df.shape[1]  #-- criando 2 variaveis para armazenar as linhas e as colunas

# print(df.columns) -- mostra o nome de todas as colunas, para saber oque cada coluna armazena

# print(f"numero de linhas: {linhas} e numero de colunas: {colunas}")

df_copy = df.copy() # -- criando uma copia para manter a original do data frame


renomear_colunas = {
    'work_year': 'ano', 
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio' : 'remoto',
    'company_location' : 'empresa',
    'company_size' : 'tamanho_empresa'
    }
df.rename(columns = renomear_colunas, inplace=True)

renomear_senoridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df["senioridade"] = df["senioridade"].replace(renomear_senoridade)
# print(df["senioridade"].value_counts())

renomear_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freelance',
    'CT': 'Contrato'
}
df["contrato"] = df["contrato"].replace(renomear_contrato)
# print(df["contrato"].value_counts())


renomear_tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Media',
    'L': 'Grande'
}
df["tamanho_empresa"] = df["tamanho_empresa"].replace(renomear_tamanho_empresa)
# print(df["tamanho_empresa"].value_counts())


renomear_remoto = {
    '0': 'Presencial',
    '100': 'Remoto',
    '50': 'Hibrido'
}
df["remoto"] = df["remoto"].replace(renomear_remoto)
# print(df["remoto"].value_counts())


# print(df["contrato"].value_counts()) # -- metodo vai contar os valores de cada categoria

# print(df.describe(include="object")) # --- count = numero de linhas || unique = valores unicos de cada tabela || top = valor que mais se repete || freq = frequencia que aquele valor se repete
# print(df.describe())

#print(df.isnull().sum()) # --- verificar se algum campo do data frame esta nulo
#print(df['ano'].unique())
# print(df[df.isnull().any(axis=1)]) # --- O resultado é uma Série (uma coluna) de valores booleanos que indica quais linhas do DataFrame original continham pelo menos um valor nulo.


df_limpo = df.dropna() # função "dropna()" ira remover todas as linhas com valores nulos do data frame, para isso nos criamos uma copia do df principal
# print(df_limpo.isnull().sum())

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))

# print(df_limpo['senioridade'].value_counts().plot(kind='bar', title="distribuição de senioridade"))

# sns.barplot(data=df_limpo, x='senioridade', y='usd')

# plt.figure(figsize=(8,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.title("Salario medio por nivel de senioridade")
# plt.xlabel("Nível de senioridade")
# plt.ylabel("Salario medio anual em USD $")

# ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
# print(ordem)


# plt.figure(figsize=(8,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
# plt.title("Salario medio por nivel de senioridade")
# plt.xlabel("Nível de senioridade")
# plt.ylabel("Salario medio anual em USD $")

# plt.figure(figsize=(8,4))
# sns.histplot(df_limpo['usd'], bins =100, kde=True)
# plt.title("distribuição dos salarios anuais")
# plt.xlabel("saalrio em usd")
# plt.ylabel("frequencia")

# plt.figure(figsize=(8,5))
# sns.boxplot(x=df_limpo['usd'])
# plt.title("boxplot salario")
# plt.xlabel("salario em usd")

# ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
# plt.title("distribuição salarial por senioridade")
# plt.xlabel("Nível de Senioridade") # O eixo X é a senioridade
# plt.ylabel("Salário em USD")      # O eixo Y é o salário

# plt.show()

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='média salarial por senioridade',
             labels={'senioridade': 'nível de senioridade', 'usd': 'média salarial anual (usd)'})

# remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# fig = px.pie(remoto_contagem,
# 	names='tipo_trabalho', 
# 	values='quantidade',
# 	title='proporção dos tipos de trabalho',
#     hole=0.5
# 	)

fig.show()