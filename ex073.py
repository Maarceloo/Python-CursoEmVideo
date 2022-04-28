tabela = ('Atletico', 'palmeiras', 'flamengo', 'bragantino',
         'fortaleza', 'corinthians', 'internacional', 'fluminense',
         'cuiaba', 'america', 'atletico go', 'sao paulo', 'ceara',
         'atletico pr', 'santos', 'bahia', 'sport', 'juventude', 'gremio',
         'chapecoense')
print('-=' * 10)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 10)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-=' * 10)
print(f'Os 4 ultimos são: {tabela[-4:]}')
print('-=' * 10)
print(f'Os times em ondem alfabetica são: {sorted(tabela)}')
print('-=' * 10)
print(f'A chapecoense esta na {tabela.index("chapecoense")+1}° posição')
