import datetime
ano = datetime.date.today().year
dic = dict()
dic['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
dic['idade'] = ano - nascimento
dic['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['ctps'] != 0:
    dic['admisao'] = int(input('Ano de contratação: '))
    dic['salario'] = int(input('Salario: R$'))
    print('-=' * 20)
    data = (dic['admisao'] + 35) - nascimento
    dic['aposentadoria'] = data
    print('-=' * 20)
else:
    print('-=' * 20)
for k, i in dic.items():
    print(f' - {k} tem o valor {i}')
