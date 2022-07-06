cont = pi = soma = man = girl = 0
while True:
    print('-'*20)
    print('CADASTRE UM USUARIO')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Resposta invalida! Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pi += 1
    if sexo in 'M':
        man += 1
    if idade < 20 and sexo in 'F':
        girl += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input(' Respostar invalida! Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if continuar in 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos {pi}')
print(f'Ao todo temos {man} homens cadastrados cadastrados')
print(f'E temos {girl} com menos de 20 anos ')
print(f'E temos {cont} cadastros realizados ')
