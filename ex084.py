lista = []
galera = []
cont = maior = menor = 0
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input(('Peso: ')))
    cont += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Resposta errada! Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
    lista.append(nome)
    lista.append(peso)
    galera.append(lista[:])
    lista.clear()
    if cont == 1:
        maior = menor = peso
    if maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
print('-=' * 20)
print(f'Ao todo, voce cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor:.2f}Kg. peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
