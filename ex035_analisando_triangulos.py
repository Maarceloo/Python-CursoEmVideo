print('=' * 30)
print('ANALISADOR DE TRIANGUILOS')
print('=' * 30)
a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('\033[34m os seguimentos podem formar um triangulo \033[m')
else:
    print('\033[031m os seguimentos nao podem formar um triangulo \033[m')
