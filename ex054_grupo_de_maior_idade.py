from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    idade = data - ano
    if idade >= 18:
        totmaior += + 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menore de idade'.format(totmenor))
