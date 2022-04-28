print('=' * 20)
print('10 TEMOS DE UMA PA')
print('=' * 20)
n1 = int(input('Primeiro termo: '))
r = int(input('razão: '))
decimo = n1 + (10 - 1) * r
for c in range(n1, decimo + r, r):
    print(c, end='-> ')
print('Acabou')
