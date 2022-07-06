lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida! Continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
listapar = []
listaimpar = []
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
