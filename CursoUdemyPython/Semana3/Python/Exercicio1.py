primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")


if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior do que {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior do que {primeiro_valor=}")
else:
    print("Valor incorreto")


# Solução do professor

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

# Lembrado estava igual o meu, porém ele adicionou o >=