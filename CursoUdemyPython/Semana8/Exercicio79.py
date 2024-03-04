# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },

]

acertos = 0
erros = 0

# for p in perguntas:
#     questão = 0
#     print(f'Pergunta: {p.get("Pergunta")}')
#     alternativas = p.get("Opções")
#     print("Opções:")
#     alternativas = p.get("Opções")
#     a,b,c,d = alternativas
#     print(a)
#     print(b)
#     print(c)
#     print(d)

#     resposta = p.get('Resposta')

#     pergunta = input("Escolha uma opção: ")

#     if resposta == pergunta:
#         acertos += 1
#         print("Você acertou!")
#     else:
#         erros += 1
#         print("Você errou!")

# print(f"Você teve {acertos} acertos e {erros} erros!")

acertos = 0
erros = 0

for p in perguntas:
    pergunta = p.get('Pergunta')
    resposta = p.get('Opções')
    print(f"Pergunta: {pergunta}")
    print()
    for resp in resposta:
        print(f'({resp})')
    
    resposta_certa = p.get('Resposta')

    usuario = input("Escolha a resposta certa: ")

    if usuario == resposta_certa:
        acertos += 1
        print("Acertou")
    else:
        erros += 1
        print("Errou!")

print(f"""Acertos: {acertos} 
Erros: {erros} """)


# Exemplo do professor

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')