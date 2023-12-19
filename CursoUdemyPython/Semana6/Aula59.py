"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  4   5  8  8  5  1  7  1  8
   40  45 64 56 30 5 28  3 16

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

usuario = input("Digite somente os números de um cpf: ")
contagem = 11
soma = []

for numero in usuario:

    contagem -= 1

    if contagem == 2:
        break

    multi = int((numero)) * contagem

    soma.append(multi)
    

valor = sum(soma)
print(valor)


    

    

