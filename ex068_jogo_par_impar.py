from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(1, 5)
    soma = jogador + computador
    resultado = soma % 2
    if resultado == 1 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('-'*30)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-=' * 30)
        cont += 1
    elif resultado == 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        print('-'*30)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-='*30)
        cont += 1
    else:
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma}')
        print('Voce perdeu!')
        print('-=' * 30)
        break
print(f'GAME OVER! Você venceu {cont} vezes.')
