lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]
print(lista1)
print(lista2)
lista3 = zip(lista1, lista2)
lista1e2somadas = ([sum(i) for i in lista3])
print(lista1e2somadas)