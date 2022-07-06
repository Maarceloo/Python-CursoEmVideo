# Coloração
cores = {'verde': '\033[32m',
         'vermelho': '\033[31m',
         'blue': '\033[34m'}
# Coleta de dados do usuario
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = float((n1 + n2) / 2)
print('Tirando {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(n1, n2, media))
# Programa
if media < 5:
    print('o aluno está {} REPROVADO'.format(cores['vermelho']))
elif media >= 7:
    print('o aluno está {} APROVADO'.format(cores['verde']))
else:
    print('O aluno esta de {} RECUPERAÇÃO'.format(cores['blue']))
