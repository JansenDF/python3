nome = 'Jansen'
idade = 34
altura = 1.75
e_maior = idade > 18
peso = 80
imc = peso / (altura * altura)

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior? ', e_maior)

print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é: {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é: {im:.2f}'.format(n=nome, i=idade, im=imc))
