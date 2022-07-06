extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um numero: '))
    print(f'voce digitou o numero {extenso[numero]}')
    continuar = str(input('Voçe quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Voçe quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('Programa finalizado! ')
