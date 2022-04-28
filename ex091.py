from random import randint
from time import sleep
from operator import itemgetter
dic = dict()
ranking = dict()
for c in range(1, 5):
    dic[f'jogador {c}'] = randint(1, 7)
print('Valores sorteados: ')
for k, c in dic.items():
    sleep(0.75)
    print(f'    O {k}° tirou {c}')
print('-=' * 20)
print('Ranking dos jogadores:')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.75)
print( 'FIM')
