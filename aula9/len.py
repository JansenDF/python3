usuario = input('Nome do usuário: ')

qtde_caractere = len(usuario)

print(f'{usuario} possui {qtde_caractere} caracteres.')

if qtde_caractere < 5:
    print('Usuário possui menos de 5 caractere!')
elif qtde_caractere > 5 and qtde_caractere < 10:
    print('Usuário possui mais de 5 e menos de 10 caracteres!')
else:
    print('Usuário poaaui mais de 10 caracteres!')