# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'João Vitor',
    'sobrenome': 'Gomes',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# Copy e Shallow copy

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)


# get é pode colocar um frase se ele não encontrar

print(pessoa.get('nome', 'None'))

# pop ele remove o item

pessoa.pop("nome")
print(pessoa)

# popoitem ele remove o ultimo item na lista

pessoa.popitem()
print(pessoa)

# update ele atualiza uma chave e pode criar uma nova chave

lista = [['robs', 'Dev'], ['Teste', '1234']]
pessoa.update(lista)

print(pessoa)