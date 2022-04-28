sexo = str(input('Informe seu sexo [M / F]: ')).upper().strip()[0]
while sexo not in 'MF':
        sexo = str(input('Dados invalidos. por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))
