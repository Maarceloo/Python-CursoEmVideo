lista = []
cont = 0
while True:
    n = int(input('Digite um valorzinho: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-=' * 20)
lista.sort()
print(f'Voce digitou os valores {lista}')
