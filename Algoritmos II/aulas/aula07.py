#Divisão e Conquista paradigma de projeto de algoritmos
# É dividido em 3 fases:
# 1- divisão O(1)
# 2- conquista  
# 3- combinação - Merge O(n)
#Basicamente divide problemas grandes em problmeas menores mais fáceis de resolver, como numa recursão.
#O algoritmo que geralmente é associado a esse paradigma é o merge-sort
#Depois de ordenar as partes pequenas (conquista), temos que juntar essas duas listas em uma só estando todos os itens ordenados (combinação)
#Vamos copiar sempre comparando os menores elementos da lista que são os primeiros das sublistas e vou caminhando nelas conforme as comparações vão acontecendo
#Essa nova lista ordenada se chama merge ou intercalação

#MERGE-SORT - O(nLogn) é o melhor para ordenar listas muito grandes, mas usa o dobro da memória
#Mas é muito melhor que O(n²)
#O(n)
import sys
import random
import time 

def merge(listaA, listaB):
    lista = []
    i = 0 
    j = 0
    while i < len(listaA) and j < len(listaB):
        if listaA[i] < listaB[j]:
            lista.append(listaA[i])
            i+=1
        else:
            lista.append(listaB[j])
            j+=1
    while i < len(listaA):
        lista.append(listaA[i])
        i+=1
    while j < len(listaB):
        lista.append(listaB[j])
        j+=1
    return lista

#O(n)
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista)//2
    listaA = mergesort(lista[:meio]) #vai dividindo até chegar no caso base, quando chega, chama a função do merge que ordena de fato
    listaB = mergesort(lista[meio:]) 
    return merge(listaA, listaB)

listaA = [1,18,33,42]
listaB = [2,13,16,46]
lista = merge(listaA, listaB)
print(lista)
lista = [18,1,33,42,16,46,2,13]
lista = mergesort(lista)
print(lista)


#Quick-sort - também tem as mesmas fases da divisão e conquista mas se comporta diferente em cada etapa
#Escolhe um elemento qualquer da lista e ele se torna o pivot (as matades vão até ele, < pivot e > pivot, mesmo que não sejam ordenados)

def partition(lista, esq, dir):
    r = random.randint(esq, dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[esq]
    for k in range(esq+1 , dir+1):
        if lista[k] < pivot:
            j+=1
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
    lista[esq] = lista[j]
    lista[j] = pivot
    return j

def quicksort(lista, esq, dir):
    if esq < dir:
        p = partition(lista, esq, dir)
        quicksort(lista, esq, p-1)
        quicksort(lista, p+1, dir)

sys.setrecursionlimit(100000)
lista = list((range(0,10000)))
quicksort(lista, 0, (len(lista)-1))
print(lista)

#Teorema: para qualque entrada o tempo esperado de execução do quick-sort é O(n log n)