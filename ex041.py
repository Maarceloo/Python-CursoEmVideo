from datetime import date
ano = (int(input('Ano de nascimento: ')))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    tabela = 'MIRIM'
elif idade <= 14:
    tabela = 'INFANTIL'
elif idade <= 19:
    tabela = 'JUNIOR'
elif idade <= 25:
    tabela = 'SÊNIOR'
else:
    tabela = 'MASTER'
print('Classificação: {}'.format(tabela))
