__author__ = 'ANDRE'
#encoding:ASCII
import os
class Pessoa:
    def __init__(self,Nome = None,Rg = None,Contato = None,VEsq = None,VDir = None):
        self.Nome = Nome
        self.Rg = Rg
        self.Contato = Contato
        self.VDir = VDir
        self.VEsq = VEsq
    def __str__(self):
        return str(self.Nome,self.Rg,self.Contato)

class BinTree:

    def __init__(self):
        self.Ref0 = None

    def GeraPessoa(self,Nome,Rg,Contato):
        return Pessoa(Nome,Rg,Contato)
################################################################################
################################################################################
    def InserirPessoas(self,Ref0,Nome,Rg,Contato):
        if Ref0 == None:
            return self.GeraPessoa(Nome,Rg,Contato)
        else:
            if Nome <= Ref0.Nome:
                Ref0.VEsq = self.InserirPessoas(Ref0.VEsq,Nome,Rg,Contato)
            else:
                Ref0.VDir = self.InserirPessoas(Ref0.VDir,Nome,Rg,Contato)
        return Ref0
################################################################################
################################################################################
    def Buscar(self,Ref0,Termo):

        if Ref0 == None:
            return 0

        else:
            if Termo < Ref0.Nome:
                return self.Buscar(Ref0.VEsq,Termo)
            else:
                return self.Buscar(Ref0.VDir,Termo)
################################################################################
################################################################################
    def MostraCad(self,Ref0):

        if Ref0 == None:
            pass

        else:
            self.MostraCad(Ref0.VEsq)
            print("%-20s %20s %12s"%(Ref0.Nome,Ref0.Contato,Ref0.Rg))
            self.MostraCad(Ref0.VDir)
################################################################################
################################################################################
def Menu():
    print("TRABALHO CONCEITOS DE PROGRAMACAO ORIENTADA A OBJETOS\n")
    print(50*"*")
    print ("M")
    print ("<1> Adicionar dados ")
    print ("<2> Imprimir")
    print ("<3> Pesquisar na arvore")
    print ("<4> Sair")
    return input("Opcao Escolhida:\n")


print("Cadastro Vazio\nInsira Dados para iniciar:")
os.system("pause")
Nome = "Andre"
Rg = "99002309"
Contato = "Enial"
##############################################################################
##############################################################################
ArvoreBin = BinTree()
Ref0 = ArvoreBin.GeraPessoa(Nome,Rg,Contato)

def principal():
##############################################################################

##############################################################################
    while True:
        os.system("pause")
        os.system("cls")
        operador = Menu()
        if operador == 1:
            Nome = ""
            Rg = ""
            Contato = ""
            print("Adicionando Dados:")
            Nome = input("Digite o nome:")
            ERg = input("Digite o Rg:")
            EContato = input("Digite o Contato:")
            ArvoreBin.InserirPessoas(Ref0,Nome,Rg = Rg + ERg,Contato = Contato + EContato)
        elif operador == 2:
            print("Mostrando Todos as Pessoas Cadastradas:")
            ArvoreBin.MostraCad(Ref0)
        elif operador == 3:
            print("Buscando Pessoa Especifica no Cadastro:")
            Busca = input("Insira O Nome da Pessoas que Deseja Encontrar:")
            if ArvoreBin.Buscar(Ref0,Busca):
                print("Encontrado")
            else:
                print("Nao Encontrado")
            input("Pressione <ENTER para continuar>")
        elif operador == 4:
            print("Fim de Programa")
            break



principal()