hora = input('Quantas horas? Por favor.')

try:
    if int(hora) >= 0 and int(hora) < 12:
        print('Bom dia!')
    elif int(hora) >= 12 and int(hora) < 18:
        print('Boa tarde!')
    elif int(hora) >= 18 and int(hora) < 24:
        print('Boa noite!')
except:
    print('Hora inválida!')