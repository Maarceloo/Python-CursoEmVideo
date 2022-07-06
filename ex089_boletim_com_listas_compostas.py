ficha = list()
media = 0
while True:
    nome = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1: '))
    n2 = float(input(('Nota 2: ')))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Resposta invalida. continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-=' * 30)
print(f'{"N°.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
