n = int(input('Digite um numero para sabe se ele é divisivel: '))
n2 = int(input('Digite mais um: '))
t = n % n2

if t == 0:
    print(f'O {n} % {n2} da {t} por tanto é par')
elif t == 1:
    print(f'O {n} % {n2} da {t} por tanto é ímpar')
