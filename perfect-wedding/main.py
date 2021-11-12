"""
Casamento Perfeito - Fundamentos de Problemas computacionais

By Jéssica Leal

"""
wedding = lambda x: print('casamento perfeito' if x else 'casamento imperfeito') #função anônima que retorna casamento perfeito caso x seja verdadeiro, caso o contrário o casamento é imperfeito

def pilha(in_data):
    S = [] #pilha
    if len(in_data) == 0:
        return wedding(True)
    try: 
        for i in in_data:
            if i in {'{','[','('}:
                S.append(i)
            elif i == ')' and S.pop() != '(':
                return wedding(False)
            elif i=='}' and S.pop() !='{':
                return wedding(False)
            elif i == ']' and S.pop() !='[':
                return wedding(False)
    except IndexError: #Esse erro é trazido quando é tentado excluir uma aspa/chave/colchete de abertura de uma lista vazia, ou seja, o elemento solicitado não existe.
        return wedding(False)
    if len(S)>0:
        return wedding(False)
    else:
        return wedding(True)
pilha([ letter for letter in input() if letter != ' ' and letter in '{}[]()'])