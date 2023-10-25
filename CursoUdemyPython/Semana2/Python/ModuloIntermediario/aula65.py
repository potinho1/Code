"""
Parametros ou argumentos: São variaveis que precisam ter algum valor

Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).


"""

# def imprimir(a,b,c):
#     print(a,b,c)

# imprimir(1,2,3)

# def saudacao(nome):
#     print(f'Olá, {nome}')

# saudacao('Potinho')

def saudacao(nome='João'):
    print(f'Olá, {nome}')

saudacao('Potinho')
saudacao()
saudacao('Vitor')