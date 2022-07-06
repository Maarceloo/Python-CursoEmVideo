d = int(input('quantos dias o carro ficou alugado?'))
km = float(input('quantos quilometros foram percorridos?'))
v = d * 60 + km * 0.15
print('O total a ser pago é de R${:.2f}'.format(v))
