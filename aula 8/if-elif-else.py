"""
Condições IF, ELIF e ELSE - Aula 4
"""

if False:
    print('Verdadeira')
elif True:
    print('agora é Verdadeira')
else:
    print('Falsa')

nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
requisitoEmprestimo = 18

if int(idade) >= requisitoEmprestimo:
    print(f'Prezado(a) {nome}, é com muita satisfação que comunicamos que vossa senhoria atende os requisitos mínimos para adquirir um empréstimo!')
else:
    print(f'Prezado(a) {nome}, lamentamos informa que vossa senhoria não atende aos requisitos mínimos para adquirir um empréstimo.')