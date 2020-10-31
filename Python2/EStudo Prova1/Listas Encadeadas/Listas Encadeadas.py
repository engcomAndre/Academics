#-*-coding:cp1252-*-

class Aluno:
    Proximo_Dado = ""
    def __init__(self,Nome = None,Matricula = None,M):
        self.Nome = Nome
        self.Matricula = Matricula
    def __str__(self):
        return ("%15s %12d"%(self.Nome,self.Rg))

Primeiro = Aluno()
Locado = Primeiro
Ultimo = Primeiro

def Menu():
    print("<1>Cadastrar Novo Aluno")
    print("<2>Mostrar Cadastro")
    print("<3>Deletar Aluno")
    print("<4>Alterar/Atualizar")
    print("<5>Cadastrar Novo Aluno")
    print("<6>Cadastrar Novo Aluno")
    return int(input("Opção Escolhida"))

def Main():
    Matricula = 0
    op = Menu()
    if op == 1:
        print(50*"*")
        print("Cadastrando Novo Aluno").upper()
        print(50*"*")
        Matricula +=1
        Nome = input("Nome do Aluno")
        Obj_Aluno = Aluno(Matricula,Nome)
        if Primeiro.Nome == None:
            Primeiro = Obj_Aluno
            Ultimo = Primeiro
        else:
            Ultimo.Proximo_Dado = Obj_Aluno
            Ultimo = Ultimo.Proximo_Dado


    elif op == 2:
        print("Mostrando Cadastro")


    elif op == 3:
        print("Não Implementado")

    elif op == 4:
        print("Não Implementado")

    elif op == 5:
        print("Não Implementado"

    elif op == 6:
        print("Não Implementado")

    else:
        print(50*"*")
        print("Valor Inválido")
        print(50*"*")




