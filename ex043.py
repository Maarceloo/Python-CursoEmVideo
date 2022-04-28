peso = float(input('Qual é o seu peso? (KG): '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    resultado = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    resultado = 'PESO IDEAL'
elif 25 <= imc < 30:
    resultado = 'SOBREPESO'
elif 30 <= imc < 40:
    resultado = 'OBESIDADE'
else:
    resultado = 'OBESIDADE MÓRBIDA tome cuidado!! '
print('Seu resultado do imc é {:.1f} sendo {}!'.format(imc, resultado))
