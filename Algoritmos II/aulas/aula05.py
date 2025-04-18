#DICIONÁRIOS

#Guardam pares de chave e valor
dicio_girias = { ##é delcarado através de chaves
    "gg" : "good game",
    "hs" : "head shot",
    "fb" : "first blood",
    "smokar" :"soltar fumacinha",
    "pinar" : "errar todos os tiros"
}

print(dicio_girias['gg']) #acessamos os valores através das chaves
dicio_girias['dronar'] = 'soltar um drone' #adicionando outro elemento
print(dicio_girias['dronar']) 
print(dicio_girias.get('dronar')) #também retorna o valor através da chave

#As chaves tem que ser obrigatoriamente um objeto imutavel e hashavel, ou seja, conseguimos aplicar uma função de hash e transformar em um valor mais simples
dicio_girias[1] = "um" #podemos usar um numero que é imutavel
dicio_girias[(2,3)] = "dois tres" #assim como tuplas

# dicio_girias[['gg', 'hf']] = 'good game, have fun' #listas são mutáveis portanto não podem ser usadas
# dicio_girias[(1, [2,3])] = 'oi' #uma tupla que possui uma lista também não é permitido, pois a tupla é imutavel mas não hashavel
#em geral tudo que é hashavel é imutável

#OPERAÇÕES COM DICIONARIOS
print("dronar" in dicio_girias) #verifica se um item está no dicionario através da chave
print('ns' not in dicio_girias) #verifica se o item não está no dicionario
#dicionarios são tabelas hash implementadas no python

for(k,v) in dicio_girias.items(): #vai listar os itens do dicionário , mas não é muito eficiente pois teria de percorre-la para cada chave e valor
    print(f'{k}: {v}')

print(list(dicio_girias.keys())) #vai listar todas as chaves do dicionario, podendo ser transformado em uma lista e ser printados
print(list(dicio_girias.values())) #vai listar todos os valores do dicionario, podendo ser transformado em uma lista e ser printados

print(dicio_girias.popitem()) #o popitem vai retirar o ultimo valor do dicionario e retorná-lo, podendo ser colocado em uma variavel ou printado
novo_dicio = {'ns':'nice shot',
              'tr': 'terroristas',
              'ct' : 'contra-terroristas',
              'pinar': 'hokama'}
dicio_girias.update(novo_dicio)#Atualiza o dicionario com o dicionario novo
for(k,v) in dicio_girias.items(): #mostrando o dicionario atualizado
    print(f'{k}: {v}')

print(len(dicio_girias)) #retorna a quantidade de elementos presentes no dicionario
dicio_girias.clear() #remove todos os itens do dicionario
print(len(dicio_girias)) #mostrando que foram limpados os elementos

#Dicionarios e tabelas hash são a mesma coisa, mas dependendo da situação pode ser mais conveniente você montar sua própria tabela


#SETS - Conjuntos
#São a mesma base de conjuntos da matemática, fazendo operações de interseção, diferença etc
#Não são ordenados, eles vão ser colocados de ordem aleatória e são sem repetições de elementos 
#Seus objetos também tem que ser hashaveis
#Também é implementado com um tipo de tabela hash
sl = {5,4,3,2,1} #são implementados com chaves também
s2 = set([2,4,6,8,10]) #também pode ser implementado com a função set que transforma um objeto iterável (lista) em conjuntos
print(sl) #imprimindo conjunto

#OPERAÇÕES
print(1 in sl) #verifica o pertencimento de um elemento no conjunto
print(1 in s2)

#UNIAO
print(sl | s2) #faz a união dos conjuntos
print(sl.union(s2)) #é uma função que também realiza a união dos conjuntos, criando um novo conjunto que tanha a união dos dois, juntando eles e tirando as repetições

#INTERSECÇÃO
print(sl & s2) #faz a interseção dos conjuntos, criando uma cópia também
print(sl.intersection(s2)) #função que tbm faz a intersecção

#Essas operações não alteram o conjunto inicial

#DIFERENÇA
print(sl - s2) #faz a difeença dos conjuntos
print(sl.difference(s2)) #faz também a diferença através da função

#DIFERENÇA SIMETRICA
print(sl ^ s2) #faz a diferença simetrica, tudo q tem em um ou em outro mas não em ambos
print(sl.symmetric_difference(s2)) #também realiza a diferença simetrica através da função

#Verifica subconjuntos
print(sl.issubset(s2)) #verifica se sl é subconjunto de s2
print(sl <= s2) #também verifica se é subconjunto

print(sl.issuperset(s2)) #verifica se um conjunto contém o outro 

#Conjuntos são objetos MUTÁVEIS
sl.add(6) #podemos adicionar elementos
print(sl)
sl.remove(3) #remove o elemento do conjunto
print(sl)
s4 = sl | s2 #seria uma forma de concatenar, mas faz a união

sl.pop() #remove elementos aleatoriamente e o retorna
print(sl)
#Não podemos usar como chave em tabelas hash, pois são mutáveis

# frozenset ele é um conjunto imutável, portanto pode ser utilizado como chave na tabela hash e dicionario
f1 = frozenset([1,2,3,4,5]) #pode ser declarado com um lista
f2 = frozenset({1,2,3,4,5}) #ou outro conjunto
print(f1)
print(f2)
#todas as operações do set funcionam aqui também
print(f1|f2) #devolve um novo frozenset
print(f1 & f2) #devolve um novo frozenset

#Mas não podemos adicionar itens diretamente no frozenset original, nem remover
dicio_girias[f1] = 'f1' #permite a inserção no dicionario, como chave
print(dicio_girias[f1])


#from collections  #é uma biblioteca que contém outros tipos de dados que podem ser uteis, como tuplas nomeadas, defaultdict, orderedDict, counter, UserDict, deque e muito mais
