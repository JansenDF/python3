#Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
def saudacao(a, b):
    return f'{a}, tudo bem {b}?'

msg = 'Ola'
nome = 'Lucas'

print(saudacao(msg, nome))

#Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
def soma(num1, num2, num3):
    return num1 + num2 + num3

print(soma(3,3,3))

#Crie uma função que receba 2 números, o primeiro é um valor e o segundo um percentual (ex. 10%). Retorne o valor do primeiro número somado do aumento do percental do mesmo.
def somaPercentual(valor, porcento):
    soma = valor + (valor * porcento)/100
    return soma

print(somaPercentual(50,5))

#Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
def divisivel(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    if num1 % 3 == 0:
        return 'Fizz'
    if num1 % 5 == 0:
        return 'Buzz'

    return num1

print(divisivel(16))