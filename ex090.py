dic = dict()
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Media de {dic["nome"]}: '))
print('-=' * 20 )
print(f' - Nome é igual a {dic["nome"]}')
print(f' - Media é igual a {dic["media"]}')
if dic['media'] >= 7:
    dic['situaçao'] = 'aprovado'
    print(f' - A situação é igual a {dic["situaçao"]}')
elif 5 <= dic['media'] < 7 :
    dic['situaçao'] = 'recuperação'
    print(f' - A situação é igual a {dic["situaçao"]}')
else:
    dic['situaçao'] = 'reprovado'
    print(f' - A situação é igual a {dic["situaçao"]}')
