frase = str(input('Digite uma frase: ')) .strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]'''
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao é um palindromo')
