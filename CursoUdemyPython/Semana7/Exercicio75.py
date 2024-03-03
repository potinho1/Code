# Crie funções que dupliquem(*2), tripliquem(*3) e quadruplicam(*4) o número recebido como parâmetro.

# Minha solução
"""
def duplicar(nunero):
    return nunero * 2

def triplicar(nunero):
    return nunero * 3

def quadruplicam(nunero):
    return nunero * 4

teste = duplicar(2)
teste2= triplicar(2)
teste3 = quadruplicam(2)
print(teste)
print(teste2)
print(teste3)
"""
# Professor

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadrplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadrplicar(2))

