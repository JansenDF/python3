"""
Entrada de dados
"""

nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")

print(f'{nome} tem {idade} anos!')

"""
Calculadora
"""
a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")
op = input("Qual operação? '+' / '-' / '*' / '/' ")

if op == '+':
    soma = int(a) + int(b)
    print(f'A soma de {a} com {b} é: {soma}')
else:
    if op == '-':
        sub = int(a) - int(b)
        print(f'A subtração de {a} com {b} é: {sub}')
    else:
        if op == '*':
            mult = int(a) * int(b)
            print(f'A multiplicação de {a} com {b} é: {mult}')
        else:
            if op == '/':
                div = int(a) / int(b)
                print(f'A divisão de {a} com {b} é: {div}')