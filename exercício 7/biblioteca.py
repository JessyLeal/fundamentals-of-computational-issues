class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)
        
    def livrosOrdenadosPeloNome(self):
            listas = [self.disponiveis, self.alugados]
            lista_geral = []
            for l in listas:
                troca = True

                while troca:
                    p = len(l)-1
                    troca = False
                    for i in range(p):
                        if l[i].nome>l[i+1].nome:
                            l[i], l[i+1]= l[i+1], l[i]
                            troca = True

            i= 0
            j = 0
            while True:
                if i==len(self.disponiveis):
                    for n in range(self.alugados.index(self.alugados[j]), len(self.alugados)-self.alugados.index(self.alugados[j])):
                        print(self.alugados[n].codigo, end=' ')
                        lista_geral.append(self.alugados[n].codigo)
                    break

                elif j == len(self.alugados):
                    for n in range(self.disponiveis.index(self.disponiveis[i]), len(self.disponiveis)-self.disponiveis.index(self.disponiveis[i])):
                        print(self.disponiveis[n].codigo, end=' ')
                        lista_geral.append(self.disponiveis[n].codigo)
                    break

                if self.disponiveis[i]<self.alugados[j]:
                    lista_geral.append(self.disponiveis[i].codigo)
                    i+=1
                else:
                    lista_geral.append(self.alugados[j].codigo)
                    j+=1
            
class Main:
    b = Biblioteca()
    q_l, *v = input().split(',')
    
    j = 0

    for livro in range(int(q_l)):
        lv = Livro(v[j], v[j+1], v[j+2])
        b.inserir(lv)
        j+=int(q_l)
    b.livrosOrdenadosPeloNome()