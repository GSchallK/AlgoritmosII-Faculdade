def selection_sort(lista):
    for i in range(len(lista) - 1, 0, -1):
        maior = i
        for j in range(i+1, len(lista)):
            if lista[j] > lista[maior]:
                maior = j
        aux = lista[i]
        lista[i] = lista[maior]
        lista[maior] = aux

#HEAP é uma estrtutura de dados que facilita a busca de valores maximos e minimos, que pode ser usado para facilitar o selection-sort
#no Max heap o pai é maior que os filhos (REGRA)
#é uma arvore binaria quase completa
#os extremos (maior valor ou menor valor) está na raiz
#Na hora de inserir um novo elemento, sempre vou comparar com o pai e trocar com ele
#Vamos implementar em um vetor e para saber quem é o filho esquerdo fazemos 2*i+1 e pro direito 2*i+2
#E para descobrir o pai de um elemento fazemos (i-1)//2

class Maxheap:
    def __init__(self, lista):
        self.dados = lista
        self.tamanho = len(lista)
        self.constroiHeap()

    def constroiHeap(self):
        #as folhas ja são heaps,j posso começar a consertar a partir do ultimo nó interno
        for i in range(self.tamanho //(2 - 1), -1 ,-1): #vai até a posição -1 pois o elemento de indice 0 na lista também precisa ser trocado
            self.desceHeap(i)

    def sobeHeap(self, i):
        if i == 0:
            return
        pai = (i-1) // 2
        if self.dados[i] > self.dados[pai]:
            self.dados[i], self.dados[pai] = self.dados[pai], self.dados[i] #faz a troca dos elementos de lugar
            self.sobeHeap(pai)

    #sempre vai inserir o mais a esquerda o possível
    def inserir(self, valor):
        self.dados.append(valor) #ao adicionar o novo elemento, eu posso ferir a regra de o pai ser sempre maior q os filhos, então precisamos reorganizar
        self.tamanho += 1
        self.sobeHeap(self.tamanho - 1) #passa o ultimo elemento para a função que é o indice do ultimo elemento
        
    def desceHeap(self, i):
        esq = 2*i + 1
        dir = 2*i+2
        maior = -1
        if esq <= self.tamanho - 1:
            maior = esq
        if dir <= self.tamanho - 1 and self.dados[dir] > self.dados[esq]:
            maior = dir
        if maior != -1 and self.dados[maior] > self.dados[i]:  #verifica se o maior dos filhos é maior do que o que estamos inserindo, se for troca
            self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i]
            self.desceHeap(maior)
    
    def remover(self):
        if self.tamanho == 0:
            return None
        maximo = self.dados[0]
        self.dados[0] = self.dados[self.tamanho - 1]
        self.dados.pop() #remove o ultimo elemento mais a direita e coloca ele na posição 0
        self.tamanho -= 1
        if self.tamanho > 0:
            self.desceHeap(0)
        return maximo

#Vamos utilizar o heap para extrair o maior para colocar na ultima posição da lista com o selection sort
#Tem complexidade O(nlogn) e não precisa de memória auxiliar, então é muito bom, mas suas constantes são maiores
    def HeapSort(self):
        for i in range(self.tamanho - 1, 0, -1):
            self.dados[0], self.dados[i] = self.dados[i], self.dados[0]
            self.tamanho -= 1
            self.desceHeap(0)

L = [18, 1, 6, 33, 42, 31]
H = Maxheap(L)
H.HeapSort()
print(H.dados)



