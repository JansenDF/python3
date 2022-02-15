num = input('Digite um número inteiro: ')
try:
    resto = int(num) % 2
    if resto == 0:
        print('O número digitado é PAR!')
    else:
        print('O número digitado é IMPAR!')
except:
    print('Você digitou um caractere INVÁLIDO!')