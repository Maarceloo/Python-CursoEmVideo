print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos voce quer mostrar? '))
print('~' * 30)
t1 = 0
t2 = 1
cont = 3
print('{} -> {} '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' Fim')
print('~' * 30)
