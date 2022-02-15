palavra = 'Python3'
numero = 1000

#''.format()
print('A palavra é: {}'.format(palavra))
#f'{}'
print(f'A palavra é: {palavra}')

#casas Decimais
print(f'{numero:5.2f}')

#Posição na String
print(palavra[0])
print(palavra[-1])
print(palavra[-2])

cont = 0
for letra in palavra:
    print(letra, cont)
    cont += 1