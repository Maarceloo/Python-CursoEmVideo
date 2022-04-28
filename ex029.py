velocidade = float(input('qual a velocidade atual do carro? '))
multa = float(velocidade - 80) * 7
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de  R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia, dirija com segurança! ')
print('tenha um bom dia, dirija com segurança')
