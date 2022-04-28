cores = {'verde' : '\033[1;32m', 'red' : '\033[1;31m'}
valor = float(input('Qual o valor do Imovel R$ '))
salario = float(input('Qual o valor do seu salario? R$ '))
ano = int(input('Em quantos anos de financiamento? '))
parcela = valor / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(valor, ano, parcela))
if parcela > salario * 30/100:
    print('seu emprestimo foi {}NEGADO'.format(cores['red']))
else:
    print('Seu emprestimo foi {}APROVADO'.format(cores['verde']))
