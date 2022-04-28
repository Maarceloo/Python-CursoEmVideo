from datetime import date
n = int(input('Ano que nasceu: '))
print('''SEXO
 [ 1 ] MASCULINO 
 [ 2 ] FEMININO''')
sexo = int(input('? '))
ano = date.today().year
idade = ano - n
print('quem nasceu em {} tem {} anos em {}'.format(n, idade, ano))
if sexo == 1 and idade > 18:
    print('voce ja deveria ter se alistado há {} Anos'.format(idade -18))
    print('seu alistamento foi em {}'.format(ano - (idade - 18)))
elif sexo == 1 and idade < 18:
    print('Ainda faltam {} anos para seu alistamento'.format(18 - idade))
    print('seu alistamento será em {}'.format(18 - idade + ano))
elif sexo == 1 and idade == 18:
    print('voce tem que se alistar IMEDIATAMENTE !')
elif sexo == 2:
    print('Pela legislação brasileira, mulheres NAO precisam se alistar obrigatoriamente.')