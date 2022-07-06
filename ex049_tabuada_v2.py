numero = int(input('Digite um numero para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} * {} = {}'.format(numero, c, (numero * c)))
