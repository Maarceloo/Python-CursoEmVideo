lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'-=' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for n, v in enumerate(lista):
    if v == max(lista):
        print(f'{n}...', end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for o, m in enumerate(lista):
    if m == min(lista):
        print(f'{o}...')
print('fim')