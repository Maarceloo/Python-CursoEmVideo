nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
letras = nome.split()
letras1 = ''.join(letras)
letras2 = len(letras1)
print('Seu nome tem {} Letras'.format(letras2))
nome1 = letras[0]
nome2 = len(letras[0])
print('seu primeiro nome é {} e ele tem {} Letras'.format(nome1, nome2))