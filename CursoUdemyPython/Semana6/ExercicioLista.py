"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ["Maria", "Helena", "Luiz", "Maria", "Helena", "Luiz"]
indice = 0

for nome in lista:
    print(f"{indice} - {nome}")
    indice += 1


# Jeito que o professor fez

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))