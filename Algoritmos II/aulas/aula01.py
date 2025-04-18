# REVISÃO DE PYTHON

print('hello world') #fazer impressão no terminal
#python é uma linguagem fracamente tipada, ou seja, ela mesma faz a dedução da tipagem dos dados

x = 10 #tipo numerico int
y = 'nome' #tipo caractere string (pode ser escrito com aspas simples ou dupla)
z = 100.0 #tipo numérico de ponto flutuante

#a função type serve para informar o tipo dos dados
print(type(x)) 
print(type(y))
print(type(z))
#Python é uma linguagem onde as variaveis todas fucionam como ponteiros. Dentro da memória, ao declararmos uma variavel como o x=10, é como se pegassemos o x e apontasse para esse valor na memória, e este valor é imutável ele sempre será 10. Ao fazermos com que x agora seja igual a 'sobrenome', estamos mudando o apontamento da variável x para esse novo dado, mas o 10 que está presente na memória continuará lá, só não tem niguém apontando para ele no momento
x = 'sobrenome'
print(type(x)) #aqui vemos que o tipo de x passa de int pra str

c = 10 + 5j #o j no python é utilizado para representar números complexos
print(type(c)) #mostra que c é do tipo complex

b = True #além disso existem também os tipos booleanos, que em python são representados mais facilmente por simplesmente TRUE e FALSE
bl = False #também é possivel ser feita a negação deles com o not true ou not false
print(type(b)) #exibe que b é do tipo bool
print(type(bl)) #exibe que bl também é do tipo bool
print(bool(z)) #a função bool serve para identificar se o dado é diferente de 0 ou não. Se for diferente, ele retornará true, mas se for igual retornará false

d = 0.00000000000000005 #em python e algumas outras linguagens de programação tem dificuldades pra lidar com numeros muito precisos 
print(d) #aqui quando mandamos printar a variavel com muitas casas decimais, ele não tem muitas deficuldades, mostra que é 5 elevado a menos 17
print(bool(d)) #e quando verificamos se ele é diferente de 0, retorna true, ou seja, ele ainda identifica que é um numero diferente de 0
#o problema começa quando tentamos fazer operações
d = d + 1 #se somamos 1 a variavel iriamos supor que o dado agora valeria 1.000000000000005
d = d - 1 #e ao subtrairmos novamente o dado voltaria a sua forma original de 0.0000000000005
print(d) #mas isso não acontece pois o python tem dificuldade pra lidar com essa precisão, assim ele faz um arredondamento e assume que o dado agora vale 0
print(bool(d)) #ao verificarmos se é diferente de 0, retorna false, pois agora o dado é de fato igual a 0. Isso pode ser resolvido com o auxilio de blibiotecas matemáticas existentes na linguagem

#As string em python funcionam de forma bem simples, podendo até mesmo ser feita operações com elas
str1 = 'hokama' #podem ser escritas com aspas simples
str2 = "Stco02" #ou com aspas duplas
str3 = """"string com varias
 linhas""" #utiliza-se 3 aspas duplas para criarmos textos com varias linhas
print(str3)
print(str1 * 10) #podemos multiplicar uma string, ou seja, fazer com que ela seja repetida determinado numero de vezes
print(str1 + str2) #podemos somá-las fazendo a concatenação delas e muito mais

#As listas são uma estrutura de dados em python que diferente dos tipos de dados comuns, são objetos mutáveis, ou seja, podem ser editadas de fato na memória. As listas aceitam todos os tipos de dados, podendo misturá-los em uma mesma lista
lista1 = [1,2,3,4] #lista de numeros
lista2 = ["hokama", "stco02"] #lista e strings
lista3 = [1, "hokama", 2, "hoks", lista1] #lista de numeros e strings e até com uma outra lista dentro de si

#Para demonstrar de fato a mutatividade desse objeto, pegamos como exemplo uma função que recebe como parametro um dado qualquer do tipo numerico, e que fará a soma de uma unidade nele
def foo(x): 
    x = x+1
    return
x = 1
foo(x) #Ao chamar a função e passar o valor 1 como o dado na variavel para função, apenas uma cópia daquela variavel será enviada a função e não a variavel em si de fato
print(x) #Portanto, quando tentamos imprimir esse valor na expectativa de que a variavel agora passe a valer 2, na verdade ela não foi alterada e continua valendo o 1 de originalmente, pois apenas a cópia foi alterada, ela mesmo é imutável  

#Agora com as listas é diferente, elas são objetos mutaveis, por tanto ao passarmos ela como argumento de uma função, elas estão sendo passadas por referência automaticamente, fazendo alterações na lista original 
def foo2(l):
    l[0] = l[0] + 1
    return
l = [1,2,3,4]
foo2(l) #ao chamarmos a função passando a lista, estamos fazendo com que seu primeiro elemento que é 1 seja somado com 1, portanto a lista agora passa a ser [2, 2, 3, 4]
print(l) #como é mostrado aqui

string1 = "banana" #aqui é mais um exemplo de como dados de tipos mais simples são imutáveis
string2 = string1 #ao fazermos essa declaração, estamos fazendo com que a string2 aponte para o mesmo endereço de memória que a string1
print(string2) #vemos que a string2 também exibe a palavra banana
print(id(string1)) #id é a função que nos informa o endereço de memória para qual uma variável aponta
print(id(string2)) #vemos que ambas possuem o mesmo endereço pois apontam para o mesmo lugar
#Entretanto, ao tentarmos fazer uma alteração em uma das variáveis, como nesse caso colocar a palavra em letra maiúscula, a linguagem fará uma cópia da string original para fazer essa alteração, pois o endereço de memória que contém a palavra 'banana' minuscula é imutável e não pode sofrer alterações dentro da memória, então é feita uma cópia modificada
string2 = string2.upper() #aqui estamos dizendo que a string2 apontrá para a cópia modificada da string1, portanto agora elas apontam para endereços de memória diferentes pois são coisas diferentes
print(string1) #demonstra que a string original permaneceu inalterada
print(string2) #demonstra que foi criada a cópia modificada com letras maiúsculas

lista4 = ['B','A','N'] #diferente do que ocorre com as variaveis de tipos comuns, se fizermos a mesma coisa com listas, as alterações acontecem para ambas, pois são objetos mutáveis
lista5 = lista4 #ao fazermos a lista 5 apontar para o mesmo endereço de memória que a lista 4
lista5[0] = 'b' #e alterarmos o primeiro elemento
print(lista4) #podemos ver que a alterção ocorreu na lista original e ambas continuam apontando para o mesmo endereço de memória


for i in range(0,10,1): #a função range serve para fazermos listagens ou repetições, podendo ser utilizado para criar laços for por exemplo. O seus argumentos são divididos em 3 partes: onde a contagem inicia, até onde ela vai e de quantos em quantos passos será feita
    print(i)

lista6 = [0,1,2,3,4,5,6,7,8,9] #se fizermos isso com listas, é pior em termos de eficiencia do que quando usando range
for i in lista6: 
    print(i)


lista7 = [1,2,3,4] #ao trabalharmos com listas podemos fazer certas manipulações com elas
lista8 = lista7[2:4] #como por exemplo, pegar pedaços especificos de uma lista, dizendo em que indice começa e em qual termina. Nesse caso estamos dizendo que a lista 8 conterá os elementos do indice 2 ao indice 4 da lista 7
print(lista8) #irá ser impresso [3, 4]

print(lista7[1]) #podemos imprimir somente o elemento de determinado indice
print(lista7[-1]) #se utilizarmos indices negativos, serão impressos de trás para frente, ou seja, do ultimo elemento para o primeiro

lista8[0] = 100 #Mas é importante ressaltar que se pegarmos apenas um pedaço de uma lista e jogá-la em outra, estará sendo criada uma cópia da lista original, ou seja, a capacidade da mutatividade é perdida e a alteração será feita apenas na cópia
print(lista7) #a lista 7 continua da mesma forma de quando foi criada


lista1 = [1,2,3,4] #demonstrando com outro exemplo
lista2 = lista1[0:] #se pegar em forma de pedaço, mesmo que seja a lista toda, ele criará outra lista, uma cópia. Ao ocultar até onde a lista irá, é o mesmo que dizer para ir até o final.
print(id(lista1)) #aqui vemos que elas ja não apontam mais pro mesmo endereço de memória
print(id(lista2)) #a lista 2 criou uma cópia em outro lugar da memória se desvinculando da lista original

print(2 in lista1) #podemos usar o operador in para verificar se um elemento está presente dentro de uma lista, retornando true se estiver e false se não estiver
print(2 not in lista1) #podemos fazer a mesma verificação com o not in para ver se o elemento não está na lista, retornando true se não estiver e false se estiver

#listas podem ser concatenadas com o operador +, mas será uma cópia, a original não é alterada

