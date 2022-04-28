from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
fim = False
while not fim:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos numeros
        [ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        resultado = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, resultado))
    elif op == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} * {} = {}'.format(n1, n2, resultado))
    elif op == 3:
        if n1 > n2:
            resultado = n1
        elif n1 < n2:
            resultado = n2
        else:
            resultado = 'Valores iguais'
        print(' Entre {} e {} o resutado é {}'.format(n1, n2, resultado))
    elif op == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        fim = True
    else:
        print('Opção invalida. tente novamente')
    print('-==' * 12)
print('Finalizando....')
sleep(1)
print('-==' * 12)
print('Fim do programa! Volte sempre! ')
