lista = []
while True:
    lista.append(int(input('Difite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida! Continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'Voce digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 nao foi encontrado')
else:
    print('O valor 5 esta na lista')