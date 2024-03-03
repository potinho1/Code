# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para um a variável e mostre o valor da variável.

def multi(*args):
    for numero in args:
        numero *= numero
    return numero

total = multi(1,2,3,4,5,6,7,8,9)
print(total)


# Crie uma função fala se um número é par ou Ímpar
# Retorne se o número é par ou Ímpar 

def par_impar(x):
    if (x % 2) / 2 == 0:
        return "Par"
    return "Ímpar" # Dica do professor, tirar o else pq se ele não cair no primeiro ele já vai pro segundo

teste = par_impar(3)
print(teste)