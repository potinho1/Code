pessoa = {}

pessoa['nome'] = 'Potinho' # Acesso chaves

# Para apagar uma chave é so colocar um  del o dicionrio e a chave: del pessoa['nome']

print(pessoa)


"""
Para tentar acessar uma chave que não existe você pode usar o .get()

exemplo:

if pessoa.get("nome") is None: # Aqui ele vai checar se tem, se tiver ele vai trazer, mas se for None ele não existe. por padrão ela já retorna None.
    print("Não existe")
else:
    print(pessoa['nome'])
"""