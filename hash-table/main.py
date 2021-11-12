def hashfunc_insert(k, i=0):

    t = k%qtd_cont 
    if containers[t][i] == None:
        containers[t][i] = k
    else: #se o container estiver ocupado, vai para o próximo espaço.
        hashfunc_insert(k, i+1)

def hashfunc_search(k, i=1):

    t = k%qtd_cont
    if i == tam_cont:
        return comp_key.append(i) 
    if containers[t][i-1] == k or containers[t][i-1] == None : 
        comp_key.append(i) 
    else:
        hashfunc_search(k, i+1)

qtd_cont, tam_cont, qtd_in, *n = map(int, input().split(' '))

containers = [[None]*tam_cont for i in range (qtd_cont)]

comp_key = [] #qtd de comparações durante a busca na tabela hash

in_data=[n[i] for i in range(qtd_in)] #dados a serem incluidos na tabela hash
rest = n[qtd_in:] #dados a serem procurados após a inserção da tabela hash

for d in range(len(in_data)): #inserção de chaves
    hashfunc_insert(in_data[d])

for r in range(len(rest)): #busca na tabela hash
    hashfunc_search(rest[r])

for i in range(len(comp_key)): 
    print(comp_key[i], end=' ')
