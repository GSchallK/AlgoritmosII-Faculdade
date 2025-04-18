import random

#Um sistema para verificação de fraudes consiste em contar em uma lista
#   de numeros, quantos terminam com 00, 01, 02 ... 99. Essa distribuição
#   normalmente vai ter uma forma constante e definida.
#A função abaixo devolve a lista com tal contagem, entretanto ela está 
#   bem ineficiente, levando quase 40 segundos para executar, uma 
#   implementação melhor vai gastar menos de 6 segundos. Melhore
#   essa função e explique.
def conta_digitos_finais(lista):
    lista_qtd_por_digito_final = [0] * 100
    for i in lista:
        lista_qtd_por_digito_final[i%100] += 1
    return lista_qtd_por_digito_final




#Não altere o programa daqui para baixo
random.seed(10)
lista = random.sample(range(0, 100000000), 10000000)
print(conta_digitos_finais(lista))

