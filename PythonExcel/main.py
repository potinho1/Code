# Se precisar fazer aleteração vai de Openpyxl
# Se for trabalhar com dados vai de Pandas

import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
# print(tabela)


# Buscar a coluna e a linha para realizar a alteração no Serviço
tabela.loc[tabela["Tipo"]=="Serviço" ,"Multiplicador Imposto"] = 1.5 

tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ResultadoProdutos.xlsx", index=False)


tabela_nova = pd.read_excel("ResultadoProdutos.xlsx")

print(tabela_nova)