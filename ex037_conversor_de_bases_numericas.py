# Coloração
cores = {'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'branco': '\033[1;30m'}
# interação do usuario
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
n1 = int(input('Sua opção: '))
# Conversao
binario = format(n, 'b')
octal = format(n, 'o')
hexa = format(n, 'x')
# programa
if n1 == 1:
    print('{} convertido para BINARIO é igual a {}{}'.format(n, cores['azul'], binario))
elif n1 == 2:
    print('{} convertido para OCTAL é igual a {}{}'.format(n, cores['amarelo'], octal))
elif n1 == 3:
    print('{} convertido para HEXADECIMAL é igual a {}{}'.format(n, cores['branco'], hexa))
else:
    print('Opçao invalida, tente novamente')
