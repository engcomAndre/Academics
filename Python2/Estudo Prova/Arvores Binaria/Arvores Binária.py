#-*-coding:cp1252-*-


class Aluno:
    def __init__(self,Matricula= None,Aluno_Direito = None,Aluno_Esquerdo = None):
        self.Matricula = Matricula
        self.Aluno_Direito = Aluno_Direito
        self.Aluno_Esquerdo = Aluno_Esquerdo
    def __str__(self):
        return ("%-0.10d %-12s "%(int(self.Matricula),self.Nome))


class Arvore_Binaria:
    def __init__(self):
        self.Aluno_Raiz = None
#################################################################
    def Cria_Aluno(self,Matricula):
        return Aluno(Matricula)
#################################################################
    def Cadastra_Aluno(self,A_Raiz,Matricula):
        if A_Raiz == None:
            return self.Cria_Aluno(Matricula)
        else:
            if Matricula <= A_Raiz.Matricula:
                A.Raiz.Aluno_Esquerdo = self.Cadastra_Aluno(A_Raiz.Aluno_Esquerdo,Matricula)
            else:
                A.Raiz.Aluno_Direito = self.Cadastra_Aluno(A_Raiz.Aluno_Direito,Matricula)
        return A_Raiz

#################################################################
    def Pesquisar(self,A_raiz,Termo_Busca):
        if A_raiz == None:
            return 0
        else:
            if Termo_Busca == A_raiz.Matricula:
                return 1
            else:
                if Termo_Busca < A_raiz.Matricula:
                    return self.Pesquisar(A_raiz.Esquerdo,Termo_Busca)
                else:
                    return self.Pesquisar(A_raiz.Direito,Termo_Busca)
##################################################################
    def Mostrar_Aluno(self,A_Raiz):
        if A_Raiz == None
            pass
        else:
            self.Mostrar_Aluno(A_Raiz.Esquerdo)
            print(A_Raiz.Matricula)
            self.Mostrar_Aluno(A_Raiz.Direito)



def Menu():
    print("\n\nEstudo de Listas Encadeadas:\n".upper())
    print("<0>Cadastrar Massa de Dados")
    print("<1>Cadastrar Novo Aluno")
    print("<2>Mostrar Cadastro")
    print("<3>Pesquisar Aluno")
    print("<4>Alterar/Atualizar")
    print("<5>Fechar Programa")
    try:
        op = int(input("Opção Escolhida"))
        if op in range(0,8):
            return op
        else:
            print("Valor Inválido")
    except ValueError:
        print("Valor Inválido")


def Main():
    Valor_Raiz = 10
    Arvore = Arvore_Binaria()
    A_raiz = Arvore_Binaria.Cria_Aluno(Valor_Raiz)
    op == Menu()
    Matricula = 0
    if op == 0:
        print("Massa de Dados Teste")
        print(50*"*")
        print("Cadastrando Novo Aluno".upper())
        print(50*"*")
        lis = ["1","5","10","15","20"]
        for i in lis:
            Obj_Aluno = Aluno(i,Matricula)
            if Primeiro.Nome == "":
                Primeiro = Obj_Aluno
                Ultimo = Primeiro
            else:
                Ultimo.Proximo_Aluno = Obj_Aluno
                Ultimo = Ultimo.Proximo_Aluno
            Matricula += 1












