import requests

link = 'https://python.gomesjoaovitor2.repl.co/pegarvendas'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total vendas'])