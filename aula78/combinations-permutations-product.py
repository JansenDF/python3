"""
Combinations, Permutations e Product - Intertools

Combinations -> Ordem não importa
Permutations -> Ordem importa
Ambos não repetem valores únicos

Product -> Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Joao', 'Maria', 'Ana', 'Jansen', 'Daniele']

for duplas in combinations(pessoas, 2):
    print(duplas)
print('--------')
for duplas in permutations(pessoas, 2):
    print(duplas)
print('--------')
for duplas in product(pessoas, repeat=2):
    print(duplas)