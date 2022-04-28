soma = cont = n = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('voce digitou {} numero e a soma entre eles foi {}'.format(cont, soma))
