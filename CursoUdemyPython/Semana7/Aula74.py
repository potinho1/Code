def criar_saudacao(saudacao): # Essa função vai ficar fixa, você pode criar a saudação, depois os nomes ficaram dinamicos
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

saudacao_bom_dia = criar_saudacao("Bom dia")
saudacao_boa_tarde = criar_saudacao("Boa tarde")
saudacao_boa_noite = criar_saudacao("Boa noite")

for nome in ["Vitor","João","José"]:
    print(saudacao_bom_dia(nome))
    print(saudacao_boa_tarde(nome))
    print(saudacao_boa_noite(nome))
