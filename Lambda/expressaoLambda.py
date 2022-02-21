lista = [
    ['P1', 6],
    ['P2', 5],
    ['P3', 30],
    ['P4', 50],
    ['P5', 16]
]

def funcao(item):
    return item[1]

print(lista)

#Usando função funcao para ordenar items pelo indice [1] (preço):
lista.sort(key= funcao, reverse=True)
print(lista)

#Usando lambda ao invés da função:
lista.sort(key= lambda item: item[1], reverse=True)
print(lista)

#Ordenar de acordo com a lista inicial
lista.sort(key= lambda item: item[0])

#Organizar a lista, sem alterar a lista Original.
#Usando a função Sorted.

print(sorted(lista, key=lambda item: item[1], reverse=True))

print(lista)
