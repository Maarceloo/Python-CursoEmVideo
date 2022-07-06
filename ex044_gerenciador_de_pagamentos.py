print('{:=^40}'.format(' LOJA MARCELO '))
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] á vista dinheiro/cheque\n'
      '[ 2 ] á vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão\n')
tipo = int(input('Qual é a sua opção? '))
if tipo == 1:
    resultado = valor - (valor * 10 / 100)
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f}'.format(valor, resultado))
elif tipo == 2:
    resultado = valor - (valor * 5 / 100)
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f}'.format(valor, resultado))
elif tipo == 3:
    print('sua compra no valor de R${:.2f} em 2x no cartao de  R${:.2f}'.format(valor, valor / 2))
elif tipo == 4:
    parcela = int(input('Em quantas parcelas? '))
    juros = valor * 20 / 100 + valor
    print('sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, juros / parcela))
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, juros))
else:
    print('Opção invalida ')
