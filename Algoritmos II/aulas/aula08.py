#TIM-SORT
#Recebe uma lista grande e divide em listas pequenas (runs)
#Utiliza o insertion-sort para ordenar esses runs, pois ele é melhor em listas pequenas
#E de 2 em dois vamos usar o mergesort para juntar esses trechos e ordenar esses pedaços maiores conforme for dando merge
#é a implementação do .sort do python
#Sua complexidade é O(n log n) também, muito bom
#Desvantagens: se a lista não dividir em multiplos de 2 dificulta seu funcionamento
#O melhor que podemos conseguir de algoritmos que usem comparação é O(n log n)
#Teorema: Qualquer algortimo de ordenação baseado em comparações terá complexidade de pior caso pior ou igual a O(n log n)


import random
import time
import sys

sys.setrecursionlimit(1000000)

def insertion_sort(lista):
  for i in range(1, len(lista)):
    j = i
    valor = lista[j]
    while j > 0 and lista[j-1] > valor:
      #lista[j-1] precisa ir pra direita
      lista[j] = lista[j-1]
      j = j - 1
    lista[j] = valor
  return lista

def merge(listaA, listaB):
  lista = []
  i = 0
  j = 0
  while i < len(listaA) and j < len(listaB):
    if listaA[i] < listaB[j]:
      lista.append(listaA[i])
      i += 1
    else:
      lista.append(listaB[j])
      j += 1
      
  while i < len(listaA):
    lista.append(listaA[i])
    i += 1
    
  while j < len(listaB):
    lista.append(listaB[j])
    j += 1
  return lista
    

def mergesort(lista):
  if len(lista) <= 1:
    return lista
    
  meio = len(lista) // 2    
  listaA = mergesort(lista[:meio])
  listaB = mergesort(lista[meio:])
  return merge(listaA, listaB)


def partition(lista, esq, dir):
  r = random.randint(esq,dir)
  aux = lista[r]
  lista[r] = lista[esq]
  lista[esq] = aux
  j = esq
  pivot = lista[esq]
  for k in range(esq+1, dir + 1):
    if lista[k] < pivot:
      j += 1
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

#IMPLEMENTANDO TIM-SORT
def timsort(lista, run):
    for x in range(0, len(lista), run):
        lista[x:x+run] = insertion_sort(lista[x:x+run])
    runsize = run
    while runsize < len(lista):
        for y in range(0,len(lista), 2*runsize):
            lista[y: y + 2 * runsize] = merge(lista[y:y+runsize], lista[y + runsize: y + 2 * runsize])
        runsize = runsize * 2
    return lista

random.seed(42)
loriginal = [random.randint(0, 2**32) for i in range(2400)]

l = loriginal.copy()
lordenado = loriginal.copy()
lordenado.sort()


l = loriginal.copy()
starttime = time.time()
l = mergesort(l)
print("Elapsed Time in Merge Sort: " + str(time.time() - starttime))
print(l == lordenado)


l = loriginal.copy()
starttime = time.time()
quicksort(l, 0, len(l)-1)
print("Elapsed Time in Quick Sort: " + str(time.time() - starttime))
print(l == lordenado)


l = loriginal.copy()
starttime = time.time()
l = insertion_sort(l)
print("Elapsed Time in Insertion Sort: " + str(time.time() - starttime))
print(l == lordenado)

l = loriginal.copy()
starttime = time.time()
l = timsort(l, 32)
print("Elapsed Time in Quick Sort: " + str(time.time() - starttime))
print(l == lordenado)

