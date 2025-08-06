import numpy as np
import pandas as pd

# criação de data frame de teste
df_salarios = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "joão", "Lucas"],
    'salario': [4000, np.nan, 5000, np.nan, 70000]
})

# calcula a media salarial e substitui os nulos pela media e arredonda os valores
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

'''calcula mediana e substitui os nulos pela media'''

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

# print(df_salarios)

# df_temperaturas = pd.DataFrame({
#     "dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
#     "temperatura": [30, np.nan, np.nan, 28, 27]
# })

# df_temperaturas["preenchido_fill"] = df_temperaturas["temperatura"].ffill()  
# # função "- ffill() -" completa coim o valor anterios os valores nulos

# print(df_temperaturas)

df_temperaturas = pd.DataFrame({
    "dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_bfill"] = df_temperaturas["temperatura"].bfill()  
# função "- ffill() -" completa coim o valor anterios os valores nulos

# print(df_temperaturas)

df_cidades = pd.DataFrame ({
    'nome': ["Ana", "Bruno", "Carlos", "joão", "Lucas"],
    'cidade': ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

df_cidades["cidade_preenchida"] = df_cidades["cidade"].fillna("Não informado") # informa para quando o valor for nulo aparecer a mensagem "Não informado"

print(df_cidades)