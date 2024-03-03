def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return f"TOTAL = {total}"

s = soma(1,2,3,44,6)
print(s)

# Para desemoacotar uma lista basta colocar um (*) no começo da variavel

# Exemplo:
"""
var = (1,2,3,4,5,6,7,8,9)
print(*var)
"""