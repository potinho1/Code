#Argumetos nomeados

#Função # nome da função # Parametros da função
def argumentos_noemados(nome="Potinho"):
    print(f"Olá {nome}")

argumentos_noemados("João")
argumentos_noemados()

# Se quiser renomear os valores você pode

# Argumentos não nomeados

def argumentos_nao_nomeados(nome):
    print(f"Olá {nome}")

# argumentos_nao_nomeados()

# Se não passar argumento ele não vai compilar, pq falta um argumento para a função

argumentos_nao_nomeados("Potinho") # Já aqui ele compila de boa, pq eu passei um argumento


# Se você passa um argumento para um prametro, mesmo que ela seja assim:
# def teste(x, y):
    #print(x + y)
# executando ela assim teste(x=1,y), ela vai dar erro pq você passou setou argumento so pra uma variavel