# Interpolação básica de strings 
# s - string 
# d e i - int 
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'Potinho'
preco = 100.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))