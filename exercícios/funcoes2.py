#Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

# def saudacao():
#     return 'Olá mundo!'

# def mestre(funcao):
#     return funcao()

# exec = mestre(saudacao)
# print(exec)

#Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Depois crie outra função que retorna que retorna qualquer função independentemente da quantidade de argumentos.

def ola(nome):
    return f'Olá {nome}'

def resultado(nome, msg):
    return f'{nome}, {msg}'

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

exec = mestre(ola, 'Jansen')
print(exec)
exec2 = mestre(resultado, 'Jansen', 'Parabéns!')
print(exec2)