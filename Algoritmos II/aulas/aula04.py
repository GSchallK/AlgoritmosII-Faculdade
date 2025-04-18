#TABELA HASH: QUADRATIC PROBING E DOUBLE HASH

class HashItem: #cria o item hash de maneira normal, passando os pares de chave e valor
	def __init__(self, key, value):
		self.key = key
		self.value = value
	
class HashTable: #cria a tabela hash com None em suas casas
	def __init__(self, size):
		self.size = size #é passado o tamanho da tabela
		self.slots = [None for i in range(size)]
		self.count = 0 #variavel para contar a quantidade de itens presentes na tabela
		
	def hash(self, s): #usa a função hash que ja conhecemos, multiplicando cada caractere da string convertido na ASCII pelo indice iniciado em 1
		mult = 1
		hash_value = 0
		for c in s:
			hash_value += mult * ord(c)
			mult += 1
		return hash_value #retorna a hash da string	
	
	def growth(self): #função utilizada para crescer a tabela caso esteja parcialmente cheia
		new_table = HashTable(self.size * 2) #cria a nova tabela
		for i in range(0, self.size):
			if self.slots[i] != None:
				new_table.put(self.slots[i].key, self.slots[i].value) #refaz o hash e coloca os itens antigos na nova tabela de dobro de tamanho
		self.size = self.size * 2 #dobra o tamanho da tabela original
		self.slots = new_table.slots #faz a tabela original apontar para a tabela nova, mantendo a tabela original
		
	def check_growth(self): #função para verificar se a tabela ja está quase cheia
		fator_carga = self.count / self.size
		if fator_carga > 0.65: #o fator de carga é 0.65, ou seja, se a tebla estiver 65% cheia
			print("aumentando o tamanho da tabela")
			self.growth() #chamamos a função para cresce-la
		
	#QUADRATIC PROBING
	def put_quad(self, key, value): #Aqui que começa a ficar diferente, pois utiliza o método do quadratic probing para resolver as colisões na hora de inserir itens na tabela
		hi = HashItem(key, value) #transformamos os pares de chave e valor em um item 
		hv = self.hash(key) % self.size #calculamos o hash tirando o modulo com o tamanho normalmente
		pos = hv #criamos um auxiliar para fazer o calculo da nova posição com quadratic probing, sem perder a posição original
		i = 1 #iniciamos a contagem dos quadrados em 1
		while self.slots[pos] != None: #passamos pelas posições até achar uma vazia
			pos = (hv + i * i) % self.size #enquanto não acha uma posição vazia, a próxima que ele vai procurar é resolvida através dessa expressão. Primeiro somamos o hash original a um quadrado e depois tiramos o módulo com o tamanho
			i = i + 1 #a variavel dos quadrados é incrementada a cada vez que a posição precisa ser recalculada pois aquela posição anterior estava ocupada			
		self.slots[pos] = hi #caso ache uma posição vazia, o item hash é colocado nela
		self.count += 1 #incrementa na variavel que conta quantos itens estão na tabela
		self.check_growth() #e checamos se a tabela ja esta quase cheia com a inserção de um novo item
	
	def get_quad(self, key): #para buscar elementos na tabela é quase a mesma lógica
		hv = self.hash(key) % self.size #calculamos o hash normalmente
		pos = hv #criamos o auxiliar para fazer os recalculos de posições
		i = 1 #e iniciamos a variavel dos quadrados em 1
		while self.slots[pos] != None: #procura na tabela até achar um posição vazia, o que siginifica que o item não está na tabela
			if self.slots[pos].key == key: #compara se a chave que procuramos está naquela posição
				return self.slots[pos].value #caso esteja, retornamos o valor associado aquela chave
			pos = (hv + i * i) % self.size #mas caso não, provavel que uma colisão tenha acontecido, então recalculamos a posição com a expressão do quadratic probing até tentar achar a chave correspondente
			i = i + 1 #soma na variavel quadratica pra acessar as posições de resolução de colisão
		return None #caso não ache o item procurado, retorna none que significa que o item não está na tabela
	
    #DOUBLE HASH
	def doublehash(self, key): #No double hash, a forma de calcular o hash nas colisões é um pouco diferente
		num = self.hash(key) #criamos um auxiliar para usar no calculo, fazemos o hash normal mas com esse resultado primário,
		return 5 - (num % 5) #fazemos a seguinte operação, escolhendo um número primo (aqui é 5) e depois subtraímos esse primo pelo módulo do hash com esse primo
	
	def put_doublehash(self, key, value): #Na função de inserir na tabela algumas coisas também são diferentes
		hi = HashItem(key, value) #criamos o item hash normalmente
		hv = self.hash(key) % self.size #e fazemos o hash normal da chave, o double só é utilizado em caso de colisão
		pos = hv #criamos um auxiliar para não perder o hash original e recalcular a posição
		i = 1 #iniciamos a variavel multiplicativa em 1
		while self.slots[pos] != None: #verificamos se a posição que queriamos colocar originalmente está livre ou nao, se não estiver, enquanto não acharmos uma posição vazia para colocar
			pos = (hv + i * self.doublehash(key)) % self.size #faremos o calculo da nova posição com o double hash, fazendo esta expressão, onde somamos o hash original com o hash do double multiplicado por i, e depois fazemos o módulo desse resultado com o tamanho da tabela
			i += 1 #acrescenta na variavel multiplicativa
		self.slots[pos] = hi #caso ache a posição vazia, colocamos o item hash nela
		self.count += 1 #acrescenta na contagem de itens da tabela
		self.check_growth() #e checa se a tabela ja está quase cheia
		
	def get_doublehash(self, key): #A função de verificar se itens estão na tabela seguem a lógica da de inserir
		hv = self.hash(key) % self.size #calculamos o hash normal 
		pos = hv #usamos um auxiliar para não perde-lo, pois ele é utilizado no calculo da double hash
		i = 1 #inicia a variavel multiplicativa em 1
		while self.slots[pos] != None: #verifica se aquela posição está vazia, o que significa que o item não está na tabela
			if self.slots[pos].key == key: #verifica se é o item que procuramos, se não for, o hash é recalculado com o double hashing
				return self.slots[pos].value #se for, o valor associado aquela chave é retornado
			pos = (hv + i * self.doublehash(key)) % self.size #se não o hash é calculado de novo com  expressão de doublehashing
			i += 1 #acrescenta na variavel multiplicativa
		return None #caso não ache, retorna none
	
	def __setitem__(self, key, value): #definimos que ao utilizar o próprio nome da tabela, conseguimos inserir os elementos
		self.put_doublehash(key, value)
	
	def __getitem__(self, key): #definimos que ao utilizar o próprio nome da tabela, conseguimos buscar os elementos
		return self.get_doublehash(key)
	
#Testando a tabela
Table = HashTable(11)
Table.put("ferreira", 2024002613)
Table["ferreira"] = 2024002613
print(Table["ferreira"])
Table["hokama"] = 2024003342
print(Table["hokama"])
Table["ga"] = 1
print(Table["ga"])
Table["ad"] = 2
print(Table["ad"])
Table["bc"] = 3
print(Table["bc"])

	
#TABELA HASH COM LISTAS
class HashTable: #Cria a tabela com o tamanho 
	def __init__(self, size):
		self.size = size
		self.slots = [[] for i in range(size)] #diferente dos outros modos, aqui iniciamos uma lista em cada casa da tabela
		
	def hash(self, s): #função pra calcular o hash, é igual os qua ja vimos
		mult = 1
		hash_value = 0
		for c in s:
			hash_value += mult * ord(c)
			mult += 1
		return hash_value #retorna o hash
		
	def put(self, key, value): #função para inserir itens na tabela
		hv = self.hash(key) % self.size #fazemos o calculo da posição normalmente, tirando o modulo do hash com o tamanho da tabela
		self.slots[hv].append((key, value)) #acessando a posição que o hash deu, appendamos o item na lista que está naquela posição
	
	def get(self, key): #função para acessar os itens 
		hv = self.hash(key) % self.size #calcula o hash
		for (k, v) in self.slots[hv]: #e procura na lista dentro daquela posição se o item está lá
			if key == k: #confere se as chaves são as mesmas
				return v #se sim, devolve o valor associado
		return None #se não acha, dentro daquela lista, quer dizer que o item não está na tabela, então retorna none
		
	
	def __setitem__(self, key, value): #definimos que ao utilizar o próprio nome da tabela, conseguimos inserir os elementos
		self.put(key, value)
	
	def __getitem__(self, key): #definimos que ao utilizar o próprio nome da tabela, conseguimos buscar os elementos
		return self.get(key)
	
#Testando a tabela		
Table = HashTable(11)
Table.put("ferreira", 2024002613)
Table["ferreira"] = 2024002613
print(Table["ferreira"])
Table["hokama"] = 2024003342
print(Table["hokama"])
Table["ga"] = 1
print(Table["ga"])
Table["ad"] = 2
print(Table["ad"])
Table["bc"] = 3
print(Table["bc"])
