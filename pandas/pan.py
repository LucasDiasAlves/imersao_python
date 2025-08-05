import pandas as pd

# url para carregar a tabela csv e atribuindo p valor da url a variavel df(data frame) 
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)

print(df.info())