'''lista = [[[], [], []],
         [[], [], []],
         [[], [], []]]
valor = coluna = par = cont = 0
while cont < 3:
    for c in range(0, 3):
        n = int(input(f'Digite um valor para {cont, c}: '))
        if n % 2 == 0:
            par += n
        if c == 0:
            lista[cont][c].append(n)
        elif c == 1:
            lista[cont][c].append(n)
        else:
            lista[cont][c].append(n)
            coluna += n
        if cont == 1:
            if valor == 0:
                valor = n
            if valor < n:
                valor = n
    cont +=1
print('-=' * 20)
print(lista[0])
print(lista[1])
print(lista[2])
print('-=' * 20)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {valor}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai += matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
