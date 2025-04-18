#Alunos: Camily Victal Finamor - 2024001197 / Luis Gustavo Riso Santos - 2024002372
#Trabalho 1 da disciplina Algoritmos e Programacao II
#------------------------------------------------------------------------------------------------------------------------------------------

#ÁRVORE BINÁRIA E CRIAÇÃO DOS NÓS

#Classe que cria os nos da arvore com o hashitem como o valor do no
class Node:
    def __init__(self, hashitem):
        self.hashitem = hashitem 
        self.esquerda = None
        self.direita = None

#Classe que cria a arvore binaria e já define o no raiz
class BinaryTree:
    def __init__(self, hashitem):
        node = Node(hashitem)
        self.raiz = node

    #Funcao da arvore biaria que insere o no na arvore, comparando alfabeticamente as chaves
    def insert(self, hashitem):
        node = Node(hashitem) 
        if self.raiz is None: 
            self.raiz = node
            return self.raiz
        else:
            atual = self.raiz
            auxRaiz = None
            while True:
                auxRaiz = atual
                if node.hashitem.chave < auxRaiz.hashitem.chave: 
                    atual = atual.esquerda
                    if atual is None:
                        auxRaiz.esquerda = node
                        return self.raiz
                else:
                    atual = atual.direita
                    if atual is None:
                        auxRaiz.direita = node
                        return self.raiz
    
    #Funcao que formata a string a ser imprimida, percorrendo a arvore no sentido pre-ordem
    def preOrder(self, raiz):
        if raiz is None:
            return "None"
        result = f"({raiz.hashitem.chave}, "
        result = result + self.preOrder(raiz.esquerda) + ", "
        result = result +  self.preOrder(raiz.direita)
        result = result + ")"
        return result

    #Funcao que faz a busca na arvore através de uma chave
    def search(self, chave):
        atual = self.raiz
        while atual is not None:
            if atual.hashitem.chave == chave:
                return atual
            elif atual.hashitem.chave > chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None
    

#------------------------------------------------------------------------------------------------------------------------------------------
#TABELA HASH

#Classe que cria o elemento hash a ser inserido na arvore
class HashItem: 
    def __init__(self, chave, valor):
        self.chave = chave 
        self.valor = valor 

#Classe que cria a tabela hash, definindo os slots como none de inicio
class HashTable: 
    def __init__(self):
        self.slots = [None for i in range(29)] 
    
    #Funcao que calcula o valor hash que eh usado para definir o slot da tabela onde o elemento estara
    def hash(self, s): 
        mult = 1
        hash_value = 0
        for c in s:
            hash_value += mult * ord(c)
            mult += 1
        return hash_value

    #Funcao que insere o elemento hash na tabela
    def put(self, chave, valor):
        hv = self.hash(chave) % 29
        if self.slots[hv] is None:
            self.slots[hv] = BinaryTree(HashItem(chave, valor))
        else:
            existing = self.slots[hv].search(chave)
            if existing:
                existing.hashitem.valor.extend(valor)
            else:
                self.slots[hv].insert(HashItem(chave, valor))

    #funcao que procura um elemento na tabela atraves de uma chave
    def get(self, chave): 
        hv = self.hash(chave) % 29
        if self.slots[hv] is not None: 
            node = self.slots[hv].search(chave)
            if node:
                print(f"{chave}")
                for item in node.hashitem.valor:
                    if isinstance(item, dict): 
                        print(f"{item['nome']} {item['quantidade']}")
                    else: 
                        print(f"{item}")
                return node
        print(f"{chave}\nNão encontrado.")
        return None

    #funcao que imprime a tabela toda
    def printTable(self):
        for i in range(0, 29):
            if self.slots[i] != None:
                elemento = self.slots[i].preOrder(self.slots[i].raiz)
                print(elemento)

#------------------------------------------------------------------------------------------------------------------------------------------
#LEITURA DE ARQUIVO

#funcao que le o arquivo com os dados de entrada
def lerArquivo(nome_arquivo, tabela_receita, tabela_itens):
    valores = []
    chave = None

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "":
                if chave and valores:
                    tabela_receita.put(chave, valores)
                    for ingrediente in valores:
                        tabela_itens.put(ingrediente["nome"], [chave])
                chave = None
                valores = []
                continue

            if chave is None:
                chave = linha
            else:
                try:
                    nome, quantidade = linha.rsplit(" ", 1)
                except ValueError:
                    continue

                elemento = {
                    "nome": nome.strip(),
                    "quantidade": quantidade.strip()
                }
                valores.append(elemento)

    if chave and valores:
        tabela_receita.put(chave, valores)
        for ingrediente in valores:
            tabela_itens.put(ingrediente["nome"], [chave])



#------------------------------------------------------------------------------------------------------------------------------------------
#MAIIN

#No main criamos as duas tabela hash (uma para a parte A do trabalho e a outra para a parte B) e fazemos a leitura do arquivo
#Tambem criamos os comandos de entrada do usuário que buscam ou imprimem os elementos
if __name__ == "__main__":
    TabelaReceita = HashTable()
    TabelaItens = HashTable()

    lerArquivo("craft.txt", TabelaReceita, TabelaItens)

    while True:
        try:
            comando = input("").strip()
        except EOFError:
            break

        if comando == "q":
            break
        elif comando == "p r":
            TabelaReceita.printTable()
        elif comando == "p i":
            TabelaItens.printTable()
        elif len(comando) > 2 and comando[:2] == "r ":
            chave = comando[2:].strip()
            TabelaReceita.get(chave)
        elif len(comando) > 2 and comando[:2] == "i ":
            chave = comando[2:].strip()
            TabelaItens.get(chave)
        else:
            print("Comando não reconhecido.")


