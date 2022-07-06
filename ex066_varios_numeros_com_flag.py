soma = cont = 0
while True:
    n = int(input('Digite um valor [999 PARA PARAR]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')
