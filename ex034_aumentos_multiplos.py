salario = float(input('Qual o salario do funcionario: '))
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'vermelho' : '\033[31m'}
if salario <= 1250:
    print('quem ganhava R${:.2f} passou a receber {}R${:.2f}{}\n'
          ''.format(salario, cores['azul'], salario * 15/100 + salario, cores['limpa']))
else:
    print('Quem ganhava R${:.2f} passou a receber {}R${:.2f}{}\n'
          ''.format(salario, cores['vermelho'], salario * 10/100 + salario, cores['limpa']))
