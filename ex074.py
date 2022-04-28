'''from random import randint
menor = maior = cont = 0
print('Os valores sorteados foram : ')
for c in range(1, 6):
    sorteados = randint(1, 10)
    cont += 1
    if cont == 1:
        maior = menor = sorteados
    if maior < sorteados:
        maior = sorteados
    elif menor > sorteados:
        menor = sorteados
    c = sorteados
    print(c, end=' ')
print(f'\nO menor valor foi {menor}')
print(f'O maior valor foi {maior}')'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
