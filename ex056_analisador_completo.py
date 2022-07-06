soma = maior = cont = 0
for dados in range(1, 5):
    print('-' * 5, '{}° PESSOA'.format(dados), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            idoso: str = nome
    if sexo == 'F':
        if idade < 20:
            cont += 1
print('A Media de idade do grupo é de {} anos '.format(soma / 4))
print(f'O homem mais velho tem {maior} anos e se chama {idoso} .')
print('Ao todo sao {} mulheres com menos de 20 anos'.format(cont))
