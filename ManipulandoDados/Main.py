# Manipular dados com o pandas

# Pegar uma base de dados e criar um DataFrame

import pandas as pd

BaseDados = {'Nome':['Potinho'],
             'Idade':[22],
             'Trabalho':['Dev']}

df_base = pd.DataFrame(BaseDados)


print(df_base)