
#Logica com MENOS linhas - FUNCIONAL

cpf = input('CPF: ')

cpfBase = cpf[:9]

cont = 10
soma = 0
for num in cpfBase:
    soma += int(num) * cont
    cont -= 1
    
    if cont < 2:
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
        if digito != int(cpf[9]):
            print('CPF inválido')
            print(cont)
            break
        else:
            cpfBase = cpf[:10]
            cont = 11
            soma = 0
            for num in cpfBase:
                soma += int(num) * cont
                cont -= 1
                if cont < 2:
                    digito = 11 - (soma % 11)
                    if digito > 9:
                        digito = 0
                    if digito != int(cpf[10]):
                        print('CPF inválido')
                    else:
                        print('CPF VÁLIDO!')


#Logica com MAIS linhas - FUNCIONAL

# contA = 0
# multiplicadorA = 10
# multiA = 0
# while contA < 9:
#     multiA += int(cpf[contA]) * multiplicadorA
#     contA += 1
#     multiplicadorA -= 1

# resA = 11 - (multiA % 11)

# if resA > 9:
#     resA = 0

# if int(cpf[9]) == resA:
#     cpfBase += cpf[contA]
# else:
#     print('CPF inválido')

# contB = 0
# multiplicadorB = 11
# multiB = 0
# while contB < 10:
#     multiB += int(cpf[contB]) * multiplicadorB
#     contB += 1
#     multiplicadorB -= 1

# resB = 11 - (multiB % 11)

# if resB > 9:
#     resB = 0

# if int(cpf[10]) == resB:
#     cpfBase += cpf[contB]
# else:
#     print('CPF inválido')
