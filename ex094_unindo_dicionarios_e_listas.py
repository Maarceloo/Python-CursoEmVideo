dic = dict()
lista = list()
mulheres = list()
cont = soma = 0
while True:
    dic['nome'] = str(input('Nome: ')).strip().title()
    dic['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dic['sexo'] not in 'MF':
        dic['sexo'] = str(input('Resposta invalida. Sexo: [M/F] ')).strip().upper()
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    if dic['sexo'] == 'F':
        mulheres.append(dic['nome'])
    lista.append(dic.copy())
    dic.clear()
    cont += 1
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while res not in 'SN':
        res = str(input('Resposta invalida! Quer continuar? [S/N]: ')).strip().upper()
    if res == 'N':
        break
media = soma / cont
print('-=' * 30)
print(f'- O grupo tem {cont} pessoas.')
print(f'- A media de idade é de {media :5.2f} anos.')
print(f'- As mulheres cadastradas foram {mulheres}')
print('- Lista de pessoas que estão acima da media: ')
for c, k in enumerate(lista):
    if lista[c]["idade"] >= media:
        print(f' nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}')
        print()
print('<< ENCERRADO >>')
