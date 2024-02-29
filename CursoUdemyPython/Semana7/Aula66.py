#Argumetos nomeados

def argumentos_noemados(nome="Potinho"):
    print(f"Olá {nome}")

argumentos_noemados("João")
argumentos_noemados()

# Se quiser renomear os valores você pode

# Argumentos não nomeados

def argumentos_nao_nomeados(nome):
    print(f"Olá {nome}")

# argumentos_nao_nomeados()

# Se não passar argumento ele não vai compilar, pq falta um argumento ou parametros para a função

argumentos_nao_nomeados("Potinho") # Já aqui ele compila de boa, pq eu passei um argumento
