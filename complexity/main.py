#CUSTOS POR INSTRUÇÃO
# • IO (instrução de entrada e saída: 30 unidades de tempo),
# • MEM (acesso à memória: 10 unidades de tempo),
# • PROCSUM (instrução de processamento: 1 unidade de tempo),
# • PROCMULT (instrução de processamento: 10 unidades de tempo)
# • LOOP X (instrução de repetição de um bloco de comandos, repete X vezes todas as instruções que estivem entre o LOOP e o respectivo FIMLOOP).

def calc(a):
    uniTempo = 0  
    loop = 1      
    for i in range (len(a)): 
        if a[i] == 'LOOP':  
            loop = int(a[i+1]) #pegar a próxima string e transformá-la em um inteiro para armazená-la na variável loop
        elif a[i] == 'FIMLOOP':
            loop = 1         # quando o loop terminar, a variável local loop volta a ser 1.
        elif a[i] == 'IO':
            uniTempo= uniTempo + (30*loop)
        elif a[i] == 'MEM' or a[i] == 'PROCMULT': #ambas instruções tem o mesmo custo, logo utilizaremos um operador lógico para evitar mais    linhas de códigos
            uniTempo= uniTempo + (10*loop)
        elif a[i] == 'PROCSUM': 
            uniTempo= uniTempo + (1*loop)
    return print(uniTempo)

calc(input().split(' ')) 