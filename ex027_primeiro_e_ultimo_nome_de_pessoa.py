nome = str(input('Digite seu nome completo: ')).strip()
new = nome.split()
print('O seu primeiro nome é {}'.format(new[0]))
print('O seu ultimo nome é {}'.format(new[len(new)-1]))

