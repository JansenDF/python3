lista = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3, 3,10,6,7,8,9,10],
    [1,2,2,4,5,3,7,8,9,8],
    [1,1,3,4,5,6,7,9,9,10],
    [1,2,3,4,5,10,7,7,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,3,3,4,5,6,7,8,9,9],
    [1,2,3,4,6,6,7,8,9,10],
    [1,2,3,4,5,7,7,8,9,10],
    [1,2,3,4,5,4,7,8,10,10],
    [1,2,3,4,5,6,7,8,9,9],
    [1,2,3,3,5,7,7,8,9,10],
]

def duplicado(param_listas):
    checados = set()

    for l in param_listas:
        if l in checados:
            return l
            break
        else:
            checados.add(l)
    return -1

for l in lista:
    print(l, duplicado(l))




