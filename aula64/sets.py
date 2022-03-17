# add (adiciona), update (atualiza), clear, discard
# Union | (une)
# Intersecion & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5}

print(type(s1)) #Tipo de s1
print(s1)
s1.add(10) # Adicionado 10 no set
print(s1)
s1.discard(2) # Retirado o numero 2 do set
print(s1)

#Fazendo cast em uma lista para set, a fim de eliminar os valores repetidos (sets nao aceitam repetições de dados)

l1 = [1,2,2,2,3,3,54,5,6,7, 'jansen', 'jansen', 'lucas', 'leo', 'daniele', 'leo']
s1 = set(l1)

print(l1)
print(s1)