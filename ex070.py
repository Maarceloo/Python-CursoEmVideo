print('-'*20)
print('      LOJA BARATÃO      ')
print('-'*20)
itens = total = caros = barato = 0
nome = ' '
while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    valor = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Opção invalida, Quer continuar? [S/N]')).strip().upper()[0]
    total += valor
    if valor > 1000:
        caros += 1
    itens += 1
    if itens == 1:
        barato = valor
        nome = produto
    if valor < barato:
        barato = valor
        nome = produto
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caros} produto custando mais de R$1000.00 ')
print(f'O produto mais barato foi {nome} que custa R${barato:.2f}')
print(f'Foram registrados {itens} produtos no sistemas de analise! ')
