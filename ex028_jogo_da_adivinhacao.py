from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n = int(input('Em que número eu pensei? '))
print('-=-' * 20)
print('PROCESSANDO...') #faz o jogador pensar
print('-=-' * 20)
sleep(2)
n1 = randint(0, 5) #faz o computador pensar
if n == n1:
    print('PARABENS! Voçê conseguiu me vencer!!!')
else:
    print('Ganhei! Eu pensei no número {} e nao no {}!'.format(n1, n))
