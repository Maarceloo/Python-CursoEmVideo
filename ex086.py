'''lista = [[[], [], []],
         [[], [], []],
         [[], [], []]]
cont = 0
while cont < 3:
    for c in range(0, 3):
        v = int(input(f'Digite um valor para {[cont, c]}: '))
        if c == 0:
            lista[cont][c].append(v)
        elif c == 1:
            lista[cont][c].append(v)
        else:
            lista[cont][c].append(v)
    cont += 1
print('-=' * 20)
print(lista[0])
print(lista[1])
print(lista[2])'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
