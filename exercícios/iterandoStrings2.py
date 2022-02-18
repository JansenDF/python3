from operator import le


frase = 'O rato roeu a roupa do rei de roma'

for letra in frase:
    if letra == 'r':
        print('R')
    else:
        print(letra)
print('########')

palavra = 'Pythn'
nova_palavra = ''

for letra in palavra:
    if letra == 't':
        nova_palavra += letra.upper()
    else:
        nova_palavra += letra.lower()
print(nova_palavra)