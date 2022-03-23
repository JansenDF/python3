from itertools import zip_longest

cidades = ['São Paulo', 'Curitiba', 'Marica', 'Brasilia']
estados = ['SP', 'PR', 'RJ', 'DF', 'RS']

estados_cidades = zip_longest(estados, cidades, fillvalue='Indefinido')

print(list(estados_cidades))