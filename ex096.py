def area(l, c):
    a = l * c
    print(f'a area de um terreno é {l}x{c} é de {a}m².')


# Programa Principal
print('Controle de terreno')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input(('Comprimento (m): ')))
area(l, c)
