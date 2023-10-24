# Formatação de strings com o método format

a = 'a'
b = 'b'
c = 1.1

print('Valor de a = {}, Valor de b = {}, Valor de c = {}'.format(a,b,c))

# Parametro nomeado 
print('Valor de a = {par1}, Valor de b = {par2}, Valor de c = {par3}'.format(par1=a,par2=b,par3=c)) # Nesse caso não importa a ordem que está, como ele está nomeado vai pegar pelo nome da variavel
