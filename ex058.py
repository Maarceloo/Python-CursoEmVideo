from random import randint
cont = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Séra que voce consegue adivinhar qual foi? ''')
computador = randint(0, 10)
jogador = int(input('Qual é o seu palpite? '))
while jogador != computador:
    cont += 1
    if jogador < computador:
        jogador = int(input('Mais... Tente mais uma vez.\nQual é seu palpite? '))
    elif jogador > computador:
        jogador = int(input('Menos... Tente mais uma vez.\nQual é seu palpite? '))
print('Acertou com {} Tentativas. Parabéns!'.format(cont))
