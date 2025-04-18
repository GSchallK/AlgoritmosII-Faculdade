#TABELAS HASH

#Utiliza uma chave e faz um cálculo (função de hash) para conseguir 
#um valor que esta entre os numeros do tamanho de um vetor para servir de índice

#Ex: 
#Chave 2024001873
#Vetor: lista[200]
#Calculo: 2024001873 % 200 = 73
#Posição: lista[73]

#Problema: pode ter um numero que o resto da divisao sera igual e gera um conflito (colisão)
#Sendo necessário resolver o conflito

#Solucao 01: mais "simples", inserir o valor no próximo indice do vetor -> Probing | Sondagem Linear
#Possivel problema: configurou-se as chaves para que tenham um padrão especifico que gerou um problema
#Ex: suas chaves terminam com um valor pequeno por um caracterista da entrada
#Com as chaves parecidas, vai ser formado uma concentracao de chaves na mesma regiao da tabela
#Fara com que você tenha que olhar muitos valores da tabela em sequencia, gerando uma pesquisa O(n) -> Problema causado pela sondagem linear

#Solucao 02: utilizando uma lista ligada
#Como eh feito?
#Cria a tabela e em cada posicao da tabela ha uma lista ligada com todos os registros que caem nessa mesma posicao
#Ex: duas chaves caem na mesma posicao -> o registro da posicao tera duas chaves e dois valores correspondentes as suas chaves
#Importante: a funcao de hash deve ter um bom espalhamento para que ocorram poucas colisões

#Problemas da Sondagem Linear:
#Pode ser que todas as posicoes da tabela fiquem preenchidas, então
#Devera ser feito um realoc para aumentar o tamanho da tabela
#Sugestao: criar um limite que caso o vetor esteja, por exemplo, 70% ocupado, dobra-se o tamanho dele
#Isso tem um custo grande, pois será necessário realocar todas as posições novamente, passando as chaves na função hash mais uma vez

#Atentar-se na criacao da funcao hash 
#Muito comum ter viezes na criacao dos registros
#Por exemplo: pode ser que todos os registros fornecam valores pares na funcao
#Isso fara com que somente as posicoes pares da tabela sejam alocadas 
#Sugestao: utilizar um numero primo mais próximo da quantidade de posições no vetor, no meu mod (%) para que os valores sejam melhores distribuidos

print(ord('h')) #A função ord imprime o valor correspondente do caractere na tabela ascii
print(sum(map(ord, 'hokama'))) #ja a função map, é como se fosse um for que percorre cada carctere da string, mapeando ela toda, juntamente da função ord convertendo para os valores numéricos da tabela e soma todos eles com a funçaõ sum
print(sum(map(ord, 'joiama'))) #mas ainda assim, ocorre de que somente essa soma da tabela ascii, ter o mesmo resultado que outra chave, causando colisão 

#Uma forma de contornar a colisão é multiplicar cada valor convertido da tabela ascci, pela posição que o caractere está na string a partir do 1 e depois fazer a soma.
def hash2(s):
        mult = 1 #multiplicação começa em 1, representa a posição de cada caractere
        hash_value = 0 #define o valor do hash como 0 inicialmente pois fazemos uma soma, isso evita erros com lixo de memória. É essa variável que receberá a soma
        for c in s: #percorro cada caractere da string, para que façamos a conversão em ascii e multiplicação de cada caractere
            hash_value += mult * ord(c) #para cada caractere, faz a soma do valor ascii convertido, multiplicado pelo "indice" da string. Essa soma é acumulada na variavel do hash_value
            mult += 1 #acrescenta no valor da variável multiplicativa, para que ela acompanhe os "indices" de cada caractere da string
            #Fazemos isso até somar os valores calculados de todos os caracteres
        return hash_value # A função retorna essa soma que é a nossa chave convertida que será usada como parte do calculo do indice, parte da função hash

print(hash2('hokama')) #testando a conversão 
print(hash2('joiama')) #testando a conversão 

print(hash2('ad')) #ainda permanecem problemas de colisão 
print(hash2('ga')) #ad e ga possuem a mesma soma 

#Tem outras aplicações de tabela hash, como conferência de dados, ou seja, se não foram corrompidos, conferência de senhas, etc

#IMPLEMENTANDO UMA TABELA HASH DE FATO
class HashItem: #essa classe irá criar o objeto hash em si, recebendo uma chave e um valor, formando o objeto a ser armazenado na tabela
    def __init__(self, key, value):
        self.key = key #definindo que o objeto receberá os atributos chave e valor
        self.value = value

class HashTable: #essa classe cria a tabela de fato, recebendo o seu tamanho e criando os slots (que é um vetor), ou seja, onde serão armazenados os pares de chave e valor
    def __init__(self, size):
        self.size = size 
        self.slots = [None for i in range(size)] #criando a tabela propriamente dita de 0 até size - 1, com valores None (vazia)
        #o for i in range(size) faz com que o i seja uma contagem passando por cada valor de 0 até o size e colocando o None como conteúdo daquela casa
        self.count = 0 #conta a quantidade de elementos da tabela, ou seja, cada vez que adicionarmos itens na tabela essa contagem é somada
    
    #Dentro da classe que cria a tabela, estarão as funções de suas principais ações: inserir, buscar, função hash(para descobrir o indice onde o par de chave e valor será colocado) e crescer tabela
    
    def hash(self, s): #é a função hash, que converte as chaves em valores inteiros que serão utilizados na função hash, assim como ja visto
        mult = 1
        hash_value = 0
        for c in s:
            hash_value += mult * ord(c)
            mult += 1
        return hash_value
    
    def growth(self): #é a função que aumenta o tamanho da tabela quando ela estiver quase cheia, dobrando o numero de slots disponiveis
        new_table = HashTable(self.size * 2) #aqui ele cria uma nova tabela, com o dobro de tamanho
        for i in range(0, self.size): #percorre a tabela original
            if self.slots[i] != None: #confere se o slot está ocupado, só executa se tiver algo no slot
                new_table.put(self.slots[i].key, self.slots[i].value) #vamos passar esse slot antigo para a nova tabela, recalculando seu indice com a função hash e atribuindo o valor a um novo slot com indice diferente da tabela original
        self.size = self.size * 2 #após guardar os valores na tabela nova com as chaves recalculadas, dobramos o tamanho da tabela original
        self.slots = new_table.slots #e fazemos a tabela original apontar pra tabela nova, assim não desperdiçamos memória
    
    def check_growth(self): #é a função que confere se a tabela está quase cheia, se estiver, ela chama a função que aumenta a tabela
        fator_carga = self.count / self.size #utilizamos um faotr de carga, que é a relação de quantidade de elementos presentes na lista (count), com a quantidade de slots(size / tamanho do vetor)
        if fator_carga > 0.65: #vamos fazer a tabela aumentar somente quando ela estiver 65% cheia, pois assim evitamos acumulo e colisões
            print('Aumentando o tamanho da tabela')
            self.growth() #se estiver 65% cheia, aumentamos ela com a função growth

    def put(self, key, value): #é a função que adiciona elementos na tabela, recebe os pares de chave e valor
        hi = HashItem(key, value) #cria o objeto/item com os pares de chave e valor
        hv = self.hash(key) % self.size #Essa é a função hash, ela tira o modulo do numero gerado no método hash pelo tamanho do vetor. O resultado desse módulo será um número entre 0 e size-1(tamanho do vetor) e será utilizado para indicar o índice onde o objeto será colocado no vetor.
        #Fazendo o processo de linear probing para fazer inserções, vendo se a posição está ocupada e se estiver, colocar na próxima livre
        while self.slots[hv]!= None: #Ou seja, enquanto aquele slot não estiver vazio, eu faço uma vericação daquela posição indicada pela função hash.
            hv = (hv + 1) % self.size #se o slot não estiver vazio, eu tiro o modulo novamente somado de 1 para que o indice se torne a próxima posição do vetor. Isso cria uma passagem circular no vetor, que quando ele chegar ao final, volta ao início.
            #o looping é quebrado quando acha uma posição vazia no vetor. Ele nunca entrará em looping infinito pois com as funções check_growth e growth, garantimos que sempre haverá espaços vazios.
        self.slots[hv] = hi #Quando ele acha o primeiro espaço vazio, coloca na posição calculada o objeto hash de chave e valor
        self.count += 1 #indica que um novo valor foi inserido na tabela
        self.check_growth() #sempre que adicionar um novo elemento, checa se a tabela está quase cheia e se precisa crescer

    def get(self, key): #é a função que confere se a chave que queremos procurar está na tabela, se estiver retorna o valor dela e se não,retorna none
        hv = self.hash(key) % self.size #recalcula o indice da chave com a função hash para descobrir onde aquele elemento estaria na tabela
        while self.slots[hv] != None: #fazemos um laço de repetição pois em casos de colisão o item que procuramos pode ter sido colocado no proximo slot, então verificamos até achar uma casa nula, que indicaria que o elemento que procuramos não está na tabela
            if self.slots[hv].key == key: #comparamos se aquele slot é onde está a chave que procuramos
                return self.slots[hv].value #se for, retornamos o valor dele
            hv = (hv + 1) % self.size #mas se não, procuramos no próximo slot, também faz uma conferência circular
        return None #se ele percorre todos os próximos slots ocupados e acaba não encontrando e chegando num slot com none, ele retornará none indicando que não encontrou o elemento


#TESTANDO A TABELA INSERINDO ELEMENTOS E BUSCANDO ELES
Table = HashTable(11)
Table.put('hokama', 'c1130')
print(Table.get('hokama'))
Table.put('rodrigo','ble')
print(Table.get('rodrigo'))
Table.put('laura', 'bli')
print(Table.get('laura'))
print(Table.get('henrique'))
Table.put('ad','blu')
Table.put('ga', 'blue')
print(Table.get('ad'))
print(Table.get('ga'))
Table.put('ga', 'blue')
Table.put('ga1', 'blue')
Table.put('ga2', 'blue')
Table.put('ga3', 'blue')
Table.put('ga4', 'blue')
Table.put('ga5', 'blue')
Table.put('ga6', 'blue')
Table.put('ga7', 'blue')

#Quando a tabela encher, vai entrar em um looping infinito pois ficará sempre procurando um lugar pra inserir novo elemento
#Para resolver isso vamos dobrar o tamanho da tabela quando a tabela estiver entre 60% a 70% cheia