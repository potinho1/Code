"""
Iterando strings com while

"""

nome = "Potinho" # Iteráveis
iterar = 0
novo_nome = ""

while iterar < len(nome):
    iterador = nome[iterar]
    letra = f"*{iterador}"
    novo_nome += letra

    iterar += 1


print(novo_nome)
    

    