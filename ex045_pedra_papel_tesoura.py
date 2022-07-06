'''from random import randint
from time import sleep
# INFORMAÇOES DO JOGADOR
print('Suas opções:\n'
      '[ 0 ] PEDRA \n'
      '[ 1 ] PAPEL \n'
      '[ 2 ] TESOURA')
# PROGRAMAÇÃO DO JOGO
jogador = int(input('Qual é sua jogada? '))
pc = randint(0, 2)
if jogador == pc:
    resultado = 'PARTIDA EMPATADA'
elif jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1:
    resultado = 'JOGADOR VENCE'
else:
    resultado = 'COMPUTADOR VENCE'
if jogador == 0:
    b = 'PEDRA'
elif jogador == 1:
    b = 'PAPEL'
elif jogador == 2:
    b = 'TESOURA'
if pc == 0:
    a = 'PEDRA'
elif pc == 1:
    a = 'PAPEL'
elif pc == 2:
    a = 'TESOURA'
else:
    print('JOGADA INVALIDA')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=-' * 10)
print('Computador jogou {}'.format(a))
print('Jogador jogou {}'.format(b))
print('-=-' * 10)
print('{}'.format(resultado))'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 11)
print('Computador jogoou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('jogada invalida')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('jogada invalida')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
