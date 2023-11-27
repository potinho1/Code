# Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.

# Se qualquer valor for considerado falso, a expresão inteira será avaliada naquele valor 
# São considerados falso (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# entrada = input("[E]ntrar / [S]air: ")
# senha_usuario = input("Digite a senha: ")

# senha_correta = '12345'

# if entrada == 'E' and senha_usuario == senha_correta:
#     print("Entrou")
# elif entrada == 'S':
#     print("Saiu")

senha = input("Digite sua senha: ") or "Sem Senha"
print(senha)