# Uma busca binária é um método de pesquisa por elementos em vetores com acessoaleatório (isto é, é possível acessar elementos diretamente pela sua posição) e ela exigeque o vetor já esteja ordenado.

from math import floor #Retorna apenas a parte inteira do número, arredondado para baixo
 
def binarysearch(ids, qtd):

    qtd +=1
    if len(ids)==1: #caso so tenha 1 elemento no vetor, retorna a qtd de comparações em 1.
        return print(qtd)
    ids.sort()    #ordena a lista

    epm =  ids[floor(len(ids)/2)] #como a lista vai de 0 a n, não é necessário fazer comparações para garantir que as regras de busca binária sejam cumpridas, tal como a lista ser um valor par, sendo 50 o epm de uma lista com 100 elementos, o valor a ser pego já será o próximo


    if epm == key:
        return print(qtd)
        
    else: 
        if epm > key:
            if ids[ids.index(epm)-1] == ids[0]: # se caso o número anterior ao ponto médio for igual ao primeiro número presente na lista, retorne a função cujo o único elemento da lista será o primeiro número. 
                return binarysearch([ids[0]],qtd)
            else:
                return binarysearch(ids[0:(ids.index(epm))], qtd)

        elif epm< key:
            if ids[ids.index(epm)+1] == ids[-1]: #se caso o número depois do ponto médio for igual ao último número presente na lista, então retorne a função cujo o único elemento da lista será o  último número presente na lista.
                return binarysearch([ids[-1]], qtd)
            else:
                return binarysearch(ids[(ids.index(epm)+1):], qtd)

key, *lista= list(map(int, input().strip().split(' ')))

binarysearch(lista, qtd = 0) #lista recebida e a quantidade de comparações
