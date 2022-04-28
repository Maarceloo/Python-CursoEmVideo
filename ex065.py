maior = menor = soma = cont = saida = 0
n = int(input('Digite um numero: '))
while saida != 'N':
    saida = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if saida == 'S':
        n = int(input('Digite um numero: '))
media = float(soma / cont)
print('Voce digitou {} numeros e a media foi {}\nO maior valor foi {} e o menor foi {}'.format(cont, media, maior, menor))
