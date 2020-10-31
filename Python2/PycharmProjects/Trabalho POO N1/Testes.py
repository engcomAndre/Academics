__author__ = 'ANDRE'
import glob
import os
class Nodo:
    def __init__(self,dado,vlrEsq = None,vlrDir = None ):
        self.dado = dado
        self.vlrEsq = vlrEsq
        self.vlrDir = vlrDir
    def __str__(self):
        return  str(self.dado)

class Arvore:

    def __init__(self):
        self.raiz = None

    def Cria_Nodo(self,valor):
        return Nodo(valor)

##################################################################################
    def InsereVlr(self,raiz,valor):
        if raiz == None:
            return self.Cria_Nodo(valor)
        else:
            if valor <= raiz.dado:
                raiz.vlrEsq = self.InsereVlr(raiz.vlrEsq,valor)
            else:
                raiz.vlrDir = self.InsereVlr(raiz.vlrDir,valor)
        return raiz

##################################################################################
    def Pesquisa(self,raiz,Tbusca):
        if raiz == None:
            return 0
        else:
            if Tbusca == raiz.dado:
                return 1
            else:
                if Tbusca < raiz.valor:
                    return self.pesquisa(raiz.vlrEsq,Tbusca)
                else:
                    return self.pesquisa(raiz.vlrDir,Tbusca)

##################################################################################
    def Imprimir(self,raiz):
        if raiz == None:
            pass
        else:
            self.Imprimir(raiz.vlrEsq)
            print(" ",raiz.dado,end = " ")
            self.Imprimir(raiz.vlrDir)


##################################################################################

##################################################################################
Dir = glob.glob("*.txt")
##################################################################################
PriRaiz = open(Dir[0],"r")
##################################################################################
ArvoreBin = Arvore()
raiz = ArvoreBin.Cria_Nodo(PriRaiz)

def menu():
    print("\nPrograma Trabalho de Python")
    print("Pressione o Opção desejada e aperte <ENTER>")
    print("[-1-] INSERIR TERMOS")
    print("[-2-] PESQUISAR TERMOS")
    print("[-3-] IMPRIMIR TERMOS")
    print("[-4-] SAIR")
    return input("OPÇÃO ESCOLHIDA :")
while True:
    os.system("cls")
    op = menu()
    if op == "1":
        for i in Dir:
            nome = ""
            for z in i(0,len(i)):
                z = z + i[]


        valor = input("DiGITE VALOR + <ENTER>")
        ArvoreBin.InsereVlr(raiz,valor)
    elif op == "2":
        ArvoreBin.Imprimir(raiz)







##################################################################################


