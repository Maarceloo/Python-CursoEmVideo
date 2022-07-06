'''import random
print('-=' * 20)
print(f'JOGA NA MEGA SENA ')
print('-=' * 20)
k = var = cont = 0
n = int(input('Quantos jogos voce quer que eu sorteie? '))
lista = []
jogo = []
jogos = []
for c in range(1, 61):
    lista.append(c)
while cont != n:
    for v in range(1, 7):
        k = random.choice(lista)
        if k not in jogo:
            jogo.append(k)
        else:
            k = random.choice(lista)
            jogo.append(k)
    jogos.append(jogo[:])
    jogo.clear()
    cont += 1
print(f'-=-=-=-= SORTEANDO {n} JOGOS -=-=-=-=-=')
while var != n:
    print(f'Jogo {var}: {jogos[var]}')
    var += 1
print(' CADA DIA MAIS DIFICIL FIM ') '''
from time import sleep
from random import randint
lista = list()
jogos = list()
print('-=' * 20)
print('     JOGA NA MEGA SENA      ')
print('-=' * 20)
quant = int(input('Quanto jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(0.75)
print('-=' * 5, 'BOA SORTE', '-=' * 5)
