Lista_usuario = []

print(Lista_usuario)

while True:
    usuario = input("""Selecione sua opção
    [i]nserir [a]pagar [l]istar [s]air: """).lower()
    
    if usuario == 'i':
        inserir_lista = input("O que deseja inserir? ").lower()
        Lista_usuario.append(inserir_lista)
    elif usuario == 'a':
        apagar_lista = input("O que deseja apagar? ").lower()
        if apagar_lista not in Lista_usuario:
            print("Não existe esse item na lista")
            continue
        else:
            Lista_usuario.remove(apagar_lista)
            print("Item pagado com sucesso!")
    
    elif usuario == 'l':
        for indice, item in enumerate(Lista_usuario):
            print(indice,item)

    elif usuario == 's':
        print("Saindo do programa!")
        break
    else:
        print("Digite uma opção valida!")
        

# Refatorar para apagar pelos indeces