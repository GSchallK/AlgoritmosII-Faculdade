#ORDENAÇÃO
#São algoritmos utilizados para ordernar diferentes tipos de dados. Existem diferentes tipos de ordenação que servem para determinados contextos e devem ser escolhidos com cuidado
#Problema geral: recebe uma lista não ordenada, a qual utilizaremos o algoritmo para ordenar e resultar numa saída crescente ou decrescente

#Esses algoritmos geralmente possuem uma Invariante de laço.
#Invariante de laço - Uma invariante de laço no contexto de algoritmos de ordenação é uma propriedade lógica que permanece verdadeira em todas as iterações de um laço (loop) durante a execução do algoritmo. Ela é usada para demonstrar a correção do algoritmo, ou seja, para mostrar que ele realmente faz o que se propõe a fazer.
# 📌 Como funciona a ideia?
# Quando analisamos um algoritmo com laços (como for, while), identificamos uma invariante que:
# É verdadeira antes da primeira iteração (inicialização),
# Permanece verdadeira após cada iteração (manutenção),
# Nos ajuda a concluir que o algoritmo está correto ao final do laço (término).
# ✅ Por que isso é importante?
# Ajuda a provar a correção do algoritmo.
# Facilita o entendimento do que o laço está garantindo a cada iteração.
#--------------------------------------------------------------------------------------------------------------------------------------------------

#BUBBLE-SORT
#Invariante de laço do Bubble-sort: Na iteração i, os ultimos i elementos são os maiores e estão ordenados. É verdadeira no começo para i igual a 0, manteremos ela ordenada no meio e isso resultará em n ultimos elementos ordenados (todos os elementos do vetor).
#Nesse algoritmo vamos comparando elementos dois a dois e se tiverem na ordem errada, são trocados entre si. O maior valor é sempre trocado até chegar no final, pois se ele é o maior valor do vetor sempre que for comparado com alguém ele irá ser jogado ao fim do vetor. Ele repete o processo a cada iteração, então após cada iteração do loop iremos reduzir o tamanho da lista a ser ordenada, pois a cada passada teremos garantia que o os ultimos elementos são os maiores e estão ordenados. No fim isso resulta num vetor todo ordenado pois ao chegar nos 2 primeiros valores da lista, ao compará-los entre si e serem trocados, resulta no vetor ordenado pois o primeiro elemento será o menor e não temos mais com quem compará-lo.
#Se chama bubble-sort pois os elementos mais leves da lista 'flutuam' (ficam no inicio) e os mais pesados caem pra baixo (final da lista), as iterações e trocas são chamadas de borbulhas.

#IMPLEMENTAÇÃO BUBBLE SORT
def bubble_sort(lista): #recebe a lista desordenada a qual vamos ordenar
    k = len(lista) - 1 #guardamos a ultima posição da lista, que é por onde vamos começar as trocas
    for i in range(k, 0, -1): #é o for que controla o tamanho da lista que estamos verificando, a cada iteração o tamanho da lista diminui pois ja inserimos um valor maior ao final da lista na posição correta
        trocou = False #verifica na primeira passada se a lista ja está ordenada ou não
        for j in range(0, i, 1): #esse é o for que controla as comparações de fato e ele vai até i que é o tamanho da lista naquele momento
            if lista[j] > lista[j+1]: #se o elemento atual for maior que seu  prómixo, eles precisam ser trocados
                aux = lista[j] #fazemos a troca com uma variável auxiliar
                lista[j] = lista[j+1]
                lista[j+1] = aux #passando o maior valor para o final da lista
                trocou = True #caso caia aqui é pq a lista não estava ordenada e trocas foram feitas
        if trocou == False: #se não trocou nada, o trocou permanece false e só é feita uma verificação, o que significa que a lista ja estava ordenada
            return #portanto podemos encerrar a função aqui, pois não precisamos perder tempo com o resto ja que a lista ja está ordenada

lista = [5, 99, 13, 18, 1, 30] #testando a ordenação da função
bubble_sort(lista)
print(lista)
#--------------------------------------------------------------------------------------------------------------------------------------------------

#INSERTION SORT
#Esse algoritmo deixa um pedaço do vetor ordenado (geralmente o inicio do vetor), ou seja, é como se dividíssimos o vetor em uma parte que ja foi ordenada no início e o restante é o que ainda não verificamos. Ele funciona pegando o primeiro elemento da lista, que sozinho já assumimos como um vetor ordenado, e então inserimos o próximo valor nesse vetor inicialmente ordenado e comparamos o valor inserido com os que ja estavam na parte ordenada e assim realizamos trocas caso este valo inserido seja menor que algum dos que ja estavam lá, ou seja, puxamos ele para a sua posição correta no começo da lista.
#Fazemos isso até chegar no ultimo elemento da lista a ser inserido e posicionado corretamente
#Invariante de laço do Insertion-Sort: na i-ésima iteração os i primeiros termos estão ordenados, então a lista toda estará ordenada na i-ésima iteração
#É um algoritmo que possui um desempenho melhor quando o vetor é pequeno.

#IMPLEMENTAÇÃO DO INSERTION SORT
def insertion_sort(lista):#recebe a lista desordenada a qual vamos ordenar
    for i in range(1, len(lista)): #começa em 1 pois assumimos que o primeiro elemento da lista (lista[0]) ja está ordenado por estar sozinho, então vamos começar a inserir o segundo elemento (lista[1])
        j = i  #é o elemento que está  sendo inserido na lista e que precisa ser comparado com os anteriores
        valor = lista[j] #utilizamos um auxiliar para guardar o valor desse elemento 
        while j > 0 and lista[j -1] > valor: #Enquanto j for maior que 0 e o valor do anterior for maior que o valor que queremos inserir
            #então as trocas precisam ser feitas e lista[j-1] (elemento anterior) precisa ir pra direita
            lista[j] = lista[j-1] #então fazemos a posição que estava o elemento que queremos inserir, receber o valor do elemento anterior
            j = j - 1 #e decrescemos j para que esse looping vá até o começo da lista, fazendo com que o elemento que estamos inserindo caminhe até que esteja em sua posição correta
        lista[j] = valor #por fim atribuímos o valor a ser inserido na posição correta


lista = [5, 99, 13, 18, 1, 30] #testando a ordenação da função
insertion_sort(lista)
print(lista)
#--------------------------------------------------------------------------------------------------------------------------------------------------

#SELECTION SORT
#Este algoritmo consiste em percorrer a lista procurando o menor valor dela e inseri-lo nas primeiras posições da lista. A cada iteração do for vamos diminuindo o tamanho da lista a ser verificada pois os primeiros elementos dela temos garantia de que ja estão ordenados, pois a cada passada inserimos o menor numero envontrado naquele momento na parte da lista que já está ordenada. Podemos fazer isso considerando o menor valor ou o maior valor.
#Invariante de laço do Selection-Sort: os i primeiros termos são os menores e estão ordenados, e percorremos o que sobrou da lista procurando o menor valor novamente e para colocá-lo na lista ja ordenada, fazendo com que na i-ésima iteração os i primeiros termos estão ordenados (todos os elementos da lista)
#Se chama selection-sort pois seleciona o menor ou maior valor da lista e o coloca na sua posição correta

#IMPLEMENTAÇÃO SELECTION-SORT
def selection_sort(lista): #recebe a lista desordenada a qual vamos ordenar
    for i in range(len(lista)): #percorre a lista toda de 0 até o fim dela, é usado para pegar o elemento atual a ser comparado e é a posição onde vamos inserir esse elemento c=de menor valor que vamos achar
        indice_menor = i #guardamos o indice da menor posição para fazermos as trocas e inicialmente assumimos que o menor valor é o primeiro da lista (lista[0])
        for j in range(i+1, len(lista)): #iniciamos portanto o for da comporação a partir do lista[1], que é usado pra pegar o elemento que será comparado com o i(atual), o j seria a lista que vai ser comparada com o i exceto o próprio i
            if lista[j] < lista[indice_menor]: #verifica se o restante da lista é < que o atual menor e se for, o indice do menor será atualizado
                indice_menor = j #atualiza o indice do menor para o do menor valor q achou no momento
        aux = lista[i] #fazemos a troca desse elementos, guardando o valor do que estava no começo da lista no momento
        lista[i] = lista[indice_menor] #inserindo o valor do que estava no indice que encontramos como o menor valor no inicio da lista
        lista[indice_menor] = aux #e colocando o valor do que estava no inicio da lista no lugar de onde estava o menor valor que encontramos
        

lista = [5, 99, 13, 18, 1, 30] #testando a ordenação da função
selection_sort(lista)
print(lista)