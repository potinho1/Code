""" Calculadora While """

while True:
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+,-,/,*): ")

    numeros_validos = None
    num_1_f = 0
    num_2_f = 0

    try:
        num_1_f = float(num_1)
        num_2_f = float(num_2)

        numeros_validos = True
        
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print("Um ou ambos dos números estão inválidos.")
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print("Operador inválido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    if operador == '+':
        print(num_1_f + num_2_f)
    elif operador == '-':
        print(num_1_f - num_2_f)
    elif operador == '/':
        print(num_1_f / num_2_f)
    elif operador == '*':
        print(num_1_f * num_2_f)




    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break

