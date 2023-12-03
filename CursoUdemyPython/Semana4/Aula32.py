"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# try:
#     usuario = int(input("Digite um número inteiro: "))
#     if (usuario % 2) == 0:
#         print("Par")
    
#     else:
#         print("Ímpar")

# except:
#     print("Número inválido!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# usuario = int(input("Digite a hora no formato inteiro (11:11), Pode colocar so (11): "))

# if usuario == 0 or usuario <= 11:
#     print("Bom dia!")

# elif usuario == 12 or usuario <= 17:
#     print("Boa tarde!")

# elif usuario == 18 or usuario <= 23:
#     print("Boa noite!")
    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuario = input("Digite o seu primeiro nome: ")

if len(usuario) <= 4:
    print("Seu nome é curto")

elif len(usuario) == 5 or len(usuario) == 6:
    print("Seu nome é normal")

elif len(usuario) > 6:
    print("Seu nome é muito grande")

