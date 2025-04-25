import random


def countingSort(lista, dAtual):
    B = [None for _ in range(0, len(lista))]
    c = [0 for _ in range(0, 10)]
    for a in lista:
        indice = (a//(10**dAtual)) % 10
        c[indice] += 1
    for i in range(1, 10):
        c[i] = c[i] + c[i-1]
    for i in range(len(lista)-1, -1, -1):
        a = lista[i]
        indice = (a//(10**dAtual)) % 10
        B[c[indice]-1] = a
        c[indice] -= 1
    return B

#Outro algoritmo de ordenação linear (O(n)) é o Radix-Sort
#RADIX SORT
#sua entrada é restrita, pois são elementos que tenham quantidades de digitos fixas
#Funciona ordenando digito a digito, começando pelos digitos menos significativos
#Essa ordenação precisa ser estável, então elementos repetidos devem seguir a ordem relativa do seu total
#Começa ordendando pela casa das unidades, depois as dezenas, centenas e adiante dependendo da quantidade de digitos
#Ele utiliza do counting sort pra ordenar esse digitos separadamente
def RadixSort(lista, qtd):
    for d in range(0, qtd):
    #Ordena A pelo digito d (estável)
        lista = countingSort(lista, d)
    return lista

lista = [315,312,214,235,181]
lista = RadixSort(lista, 3)
print(lista)


#Outro algoritmo de ordenação linear é o Bucket-Sort
#Bucket-Sort
#Seus valores de entrada permitem numeros fracionario mas estão limitados entre valores de 0 a 1 e precisam ser uniformemente distribuidos
#Divide os valores em baldes(vetores ou listas ligadas) que tem um limite(Ex: 0 a 0,2) e ordena esse baldes depois com um outro algoritmo de ordenação, como o insertion sort

def insertion_sort(lista):
    for i in range(1, len(lista)): 
        j = i  
        valor = lista[j]
        while j > 0 and lista[j -1] > valor: 
            lista[j] = lista[j-1] 
            j = j - 1 
        lista[j] = valor


def bucketSort(lista):
    n = len(lista)
    buckets = [[] for _ in range(n)]
    for numero in lista:
        indice = int(numero * n)
        buckets[indice].append(numero)
    for b in buckets:
        insertion_sort(b)
    indice = 0
    for b in buckets:
        for numero in b:
            lista[indice] = numero
            indice += 1

random.seed(42)
A = [random.random() for _ in range(5)]
bucketSort(A)
print(A)