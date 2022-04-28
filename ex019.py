import random
a = str(input('para realizarmos o sorteio, diga o nome do primeiro aluno:'))
b = str(input('do segundo:'))
c = str(input('do terceiro:'))
d = str(input('do quarto aluno:'))
s = [a, b, c, d]
print('o aluno sortedo foi o {}'.format(random.choice(s)))