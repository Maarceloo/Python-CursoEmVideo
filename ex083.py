'''aberto = fechado = 0
teste = str(input('Digite uma expressão: '))
for n in teste:
    if n == '(':
        aberto += 1
    if n == ')':
        fechado += 1
total = aberto + fechado
if total % 2 == 0:
    print('Sua expressao está correta!')
else:
    print('Sua expressao está errada!')'''

expr = str(input('Digite a sua expresão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
