x = 5

def escopo():
    x = 10
    def escopo2():
        y = 4
        print(y)
    escopo2()
    print(x)

escopo()
print(x)

# Variaveis definida no começo no codigo, pode ser acessada no codigo iteiro, pq seria as variaveis globais.

# já variaveis que a gente cria na função ela pertence so pra função, você consegue acessar ela no na função, fora da função não. 

# Dentro da função você pode atribuir o nome de uma variavel igual a uma varivel global.

# se quiser que uma variavel dentro de uma função, seja global você pode fazer assim:
#def var_global():
    #global x
    #print(x)
#var_global()

# Dessa forma a variavel que está no inicio do codigo ela vai entrar como global pra aquela função.

# Depois que executar a vairavel global da função, você vai poder manipiular ela. Então se x comecou com 1 e você definir uma varivel x = 10. logo x vai valer 10.