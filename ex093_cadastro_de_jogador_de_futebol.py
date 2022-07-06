dic = dict()
lista = list()
soma = 0
dic['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    soma += gol
    lista.append(gol)
dic['gols'] = lista
dic['total'] = soma
print('-=' * 20)
print(dic)
print('-=' * 20)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {dic["nome"]} jogou {partidas} partidas. ')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {lista[c]} gols.')
print(f'Foi um total de {dic["total"]}')
