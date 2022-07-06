for c in range(1, 5):
    valor = int(input('Digite um numero: '))
    if c == 1:
        a = valor
    if c == 2:
        b = valor
    if c == 3:
        d = valor
    if c == 4:
        e = valor
tupla = a, b, d, e
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição')
else:
    print('O valor 3 nao foi encontrado')
print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end='')
