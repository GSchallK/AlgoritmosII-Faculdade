#Comparar igualdade das listas com == (compara igualdade de elementos)
lista1 = [1, 2, 3, 4]
lista3 = [1, 2, 3, 4]
if lista1 == lista3:
    print("Lista iguais")
else:
    print("Lista diferentes")

#comparar igualdade com is (compara igualdade de enderços de memória)
if lista1 is lista3:
    print("lista1 e lista3 sao o mesmo objeto")
else:
    print("lista1 e lista3 são objetos distintos")

#Existe o "is not"
if lista1 is not lista3:
    print("lista1 e lista3 são objetos distintos")
else:
    print("lista1 e lista3 são o mesmo objeto")

#strings tbm são imutaveis, se tentar tratar elas como listas ainda assim não consegue fazer alterações sem criar copias
#Utilizar o append para inserir no final de uma lista, irá inserir na lista original o que é mais eficiente que a concatenação 
# concatenações com o operador de + criará uma cópia 
# usar o extend para extender uma lista é permitido pela mutatividade, ou seja, a alteração será feita na lisa original sem criar cópias

#Os operadores lógico and e or funcionam da mesma forma que nas outras linguagens, avaliando se sentenças são ou não verdadeiras
if 1 < 2 and 3 >= 3 and not 5 > 6 or 7 < 3:
    print("passou no if")  


#TUPLAS
tupla1 = (10,30,20)
tupla2 = ('hokama', 10)
tupla3 = ('hokama', 10) #nesse caso tupla 2 e tupla3 são o mesmo objeto mesmo sem fazer a atribuição
print(id(tupla2))
print(id(tupla3))
print(tupla2[1])
# tupla2[1] = 20 não pode
print(tupla2[-1])
print(tupla1[1:]) #faz uma cópia

lista6 = [1,2]
lista6.extend((3,4,5))
print(lista6)


lista6.append((3,4,5)) #o append entende a tupla como um elemento unico
print(lista6)

#len, min, max de listas
print(len(lista6))

#tuplas podem ser concatenadas com o operador +
tupla6 = (1,10) + (2,20)
print(tupla6)

#a tupla dentro de uma lista não pode ser alterada
#ja a lista dentro de uma tupla pode pois a lista é mutavel, podendoaté mesmo fazer operações como append e extend
tupla7 = (1,2, [3,4])
print(tupla7)
print(id(tupla6))
tupla7[2][0] = 30
print(tupla7)
print(id(tupla7))



