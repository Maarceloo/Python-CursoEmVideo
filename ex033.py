'''valor1 = int(input('Digite primeiro valor: '))
valor2 = int(input('digite segundo valor : '))
valor3 = int(input('Digite terceiro valor: '))
if valor1 > valor2 and valor1 > valor3:
    print('O valor maior é {}'.format(valor1))
if valor2 > valor1 and valor2 > valor3:
    print('O valor maior é {}'.format(valor2))
if valor3 > valor1 and valor3 > valor2:
    print('O valor maior é {}'.format(valor3))
if valor1 < valor2 and valor1 < valor3:
    print('O valor menor é {}'.format(valor1))
if valor2 < valor1 and valor2 < valor3:
    print('O valor menor é {}'.format(valor2))
if valor3 < valor1 and valor3 < valor2:
    print('O valor menor é {}'.format(valor3))'''

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
# menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# maior valor
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('o maior valor é {} '.format(maior))
print('o menor valor é {} '.format(menor))