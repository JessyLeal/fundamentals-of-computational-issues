
# ao invés de retornar um valor inteiro baseado na sequência de fibonacci, a função retornará uma string

def rec(n):
    if n == 0:
        return 'b'
    elif n == 1:
        return 'a'
    else:
        return rec(n-1)+ rec(n-2)

print(rec(int(input())))

