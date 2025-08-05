import pandas as pd

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

print(df.describe(include="object")) # --- count = numero de linhas || unique = valores unicos de cada tabela || top = valor que mais se repete || freq = frequencia que aquele valor se repete
print(df.describe())