# Funções de primeira classe

def saudacao(msg, nome, idade):
    return f"{msg}, seu nome é {nome} e  você tem {idade}"

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "Olá Mundo!", "Potinho", 23)
print(v)


"""
Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""