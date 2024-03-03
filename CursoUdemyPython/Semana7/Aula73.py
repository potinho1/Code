# Funções de primeira classe

def saudacao(msg, nome, idade):
    return f"{msg}, seu nome é {nome} e  você tem {idade}"

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "Olá Mundo!", "Potinho", 23)
print(v)