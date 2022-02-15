import fractions


frase = 'O rato roeu a roupa do rei de roma'
tamanhoFrase = len(frase)

nova_frase = ''
cont = 0
while cont < tamanhoFrase:
    letra = frase[cont]
    if cont == 0:
        nova_frase += letra.upper()
    elif frase[cont] == 'r':
        nova_frase += 'l'
    else:
        nova_frase += letra
    cont += 1
print(nova_frase)
