# Faça um programa que mostre a letra que mais apareceu na frase

frase = input("Digite uma frase para eu descobrir a letra que mais apareceu: ")


index = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while index < len(frase):
    letra_atual = frase[index]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    index += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_atual}" que apareceu '
    f'{qtd_apareceu_mais_vezes_atual}x'
)