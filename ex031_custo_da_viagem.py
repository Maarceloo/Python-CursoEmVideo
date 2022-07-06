distancia = float(input('Qual a distancia da sua viagem: '))
print('Você esta preste a fazer uma viagem de {:.1f}Km'.format(distancia))
if distancia <=200:
    valor = float(distancia * 0.50)
    print('E o valor da sua passagem é de R${:.2f} '.format(valor))
else:
    valor2 = float(distancia * 0.45)
    print('E o valor da sua passagem é de R${:.2f}'.format(valor2))
