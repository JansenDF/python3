secreta = 'fabrica'

acertos = []

while True:
    chute = input('Digite uma letra: ').lower()

    acertos.append(chute)

    if chute in secreta:
        print('Acertou!')
    else:
        print('Errou')
        acertos.pop()
    
    temp = ''
    for letra in secreta:
        if letra in acertos:
            temp += letra
        else:
            temp += '*'
    if temp == secreta:
        print('Você ganhou!')
        break

    print(acertos)
    print(temp)