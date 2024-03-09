letras = set()

while True:
    usuario = input("Digite uma letra: ")
    letras.add(usuario.lower())

    if "l" in letras:
        print("PARABENS")
        break

    print(letras)

