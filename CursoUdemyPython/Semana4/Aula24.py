# Operadores in e not in 
# Strings são intráveis 
#  0 1 2 3 
# J O Ã O 
# -3-2-1-0

nome = 'João'
print(nome[2])
print(nome[-2])

print('J' in nome)
print('o' not in nome)


print(10 * '-')


usuario = input("Digite seu nome: ")
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in usuario:
    print(f"{encontrar} está em {usuario}")
else:
    print(f"{encontrar} não está em {usuario}")