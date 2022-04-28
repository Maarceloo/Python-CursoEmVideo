'''import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))'''

from math import radians, sin, cos, tan
angulo = float(input('digite um angulo: '))
seno = sin(radians(angulo))
print('o angulo {} tem a SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))