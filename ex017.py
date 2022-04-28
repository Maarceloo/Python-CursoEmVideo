'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('qual a medida do cateto oposto?'))
ca = float(input('qual a medida do cateto adjacente?'))
h = math.hypot(co, ca)
print('O valor da hipotenusa é de {:.2f}'.format((h)))