n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('terceiro segmento: '))
if n1 == n2 == n3:
    resultado = 'EQUILATERO'
    teste = 'PODEM FORMAR'
elif n1 == n2 != n3 or n1 == n3 != n2:
    resultado = 'ISOCELES'
    teste = 'PODEM FORMAR'
elif n1 != n2 != n3 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    resultado = 'ESCALENO'
    teste = 'PODEM FORMAR'
else:
    resultado = ''
    teste = 'NAO PODEM FORMAR'
print('Os seguimentos acima {} UM TRIANGULO {}'.format(teste, resultado))
