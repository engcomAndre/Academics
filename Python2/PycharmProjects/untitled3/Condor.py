__author__ =\'ANDRE'
#encoding:UTF-8
import pickle
import random
import msvcrt
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
            if Termo in (Ref0.Nome):
                print("Encontrado:")
                print("Nome = "),str(Ref0.Nome)
                print("Rg = "),str(Ref0.Rg)
                print("Contato = "),str(Ref0.Contato)
                print("")
                os.system("pause")
                pass

            else:
                if Termo < Ref0.Nome or Termo < Ref0.Rg or Termo < Ref0.Contato:
                    return self.Buscar(Ref0.VEsq,Termo)
                else:
                    return self.Buscar(Ref0.VDir,Termo)


################################################################################
################################################################################
    def MostraCad(self,Ref0,Termo):

        if Ref0 == None:
            return 0
        else:
            if Termo == 1:
                self.MostraCad(Ref0.VEsq,Termo)
                print("Nome ="),str(Ref0.Nome)
                print("Rg ="),str(Ref0.Rg)
                print("Contato ="),str(Ref0.Contato)
                print("")
                self.MostraCad(Ref0.VDir,Termo)
            else:
                print("Termo = "),Termo
                self.MostraCad(Ref0.VEsq,Termo)
                if Termo in (Ref0.Nome or Ref0.Rg):
                    print("Nome ="),str(Ref0.Nome)
                    print("Rg ="),str(Ref0.Rg)
                    print("Contato ="),str(Ref0.Contato)
                    print("")
                    self.MostraCad(Ref0.VDir,Termo)
                    pass
                else:
                    return 0



################################################################################
################################################################################
def Entradados(Text,Tipo):
    os.system("cls")
    Nome = ""
    aux = ""
    while aux != "\r":
        print(Text)
        print (Tipo,"=",Nome)
        aux = msvcrt.getch()
        if aux == "\x08":
            aux = len(Nome)-1
            Nome = Nome[0:aux]
            os.system("cls")
        else:
            Nome = Nome + aux
            os.system("cls")
    else:
        return Nome
################################################################################
################################################################################

def Menu():
    os.system("cls")
    print("TRABALHO CONCEITOS DE PROGRAMACAO ORIENTADA A OBJETOS\n")
    print(50*"*")
    print ("Escolha o que Deseja Fazer:")
    print ("<0> Adicionar dados(MASSA DE DADOS) ")
    print ("<1> Adicionar dados ")
    print ("<2> Imprimir")
    print ("<3> Pesquisar na Arvore")
    print ("<4> Salvar Arquivo")
    print ("<5> Sair")
    print("Opcao Escolhida:\n")

    return msvcrt.getch()
################################################################################
################################################################################

def geraobj(esc):
    (nome,nome1,nome2,nome3) = ("","","","")
    lista1 = ['Andre','Cristina','Angelo','Alexandre','Ana Maria','Luis','Carolina','Isabel','Renata','Yasmin']
    lista2 = ['Vieira','da','de','Teixeira','da','de','Luz','Santos','Sales','Tabosa','Almeida','Cristino','Macedo','Oliveira','Maria']
    lista3 = ['Silva','Alberto','Craveiro','Lazaro','Camurca','Gomes','Cirineu','Nazareno','De Luca','Maceio','Novalgino','Mufumba']
    lista4 = ["hotmail","gmail","bol","ig","uol","secrelnet","baydenet","NAO INFORMADO"]
    nome1 = lista1[random.randint(0,len(lista1)-1)]
    nome2 = lista2[random.randint(0,len(lista2)-1)]
    nome3 = lista3[random.randint(0,len(lista3)-1)]
    op = random.randint(0,len(lista4)-1)
    if esc == "0":
        nome = nome1 + " " + nome2+ " " +nome3
        rg = random.randint(0000000000,9999999999)
        if op == 7:
            contato = lista4[7]
            return [nome,str(rg),contato]
        else:
            contato = nome1 + nome2 + "@" + lista4[op]+".com.br"
            return [nome,str(rg),contato]

    elif esc == "1":
        nome = nome1 + " " + nome2+ " " +nome3
        return nome
    elif esc == "2":
        return random.randint(0000000000,9999999999)
    elif esc == "3":
        if op == 7:
            nome = lista4[7]
            return nome
        else:
            nome = nome1 + nome2 + "@" + lista4[op]+".com.br"
            return nome
    else:
        print("VALOR INVALIDO")

################################################################################
################################################################################

################################################################################
################################################################################

#
# print("Cadastro Vazio\nInsira Dados para iniciar:")
# os.system("pause")
# Nome = Entradados("Digite o Nome :","Nome")
# Rg = Entradados("Digite o Numero do RG :","RG")
# Contato = Entradados("Digite o Numero de Contato","Contato")
##############################################################################
##############################################################################
ArvoreBin = BinTree()
a = geraobj("0")
Ref0 = ArvoreBin.GeraPessoa(a[0],a[1],a[2])
def principal():
    while True:
        operador = Menu()
        if operador == "0":
            print("Gerando Cadastro de Massa de Dados")
            aux = input("Digite Numero de Cadastros que deseja Criar")
            for i in range(0,int(aux)):
                a = geraobj("0")
                ArvoreBin.InserirPessoas(Ref0,a[0],a[1],a[2])
        elif operador == "1":
            os.system("cls")
            print("Adicionando Dados:")
            Nome = Entradados("Digite o Nome :","Nome")
            Rg = Entradados("Digite o Numero do RG :","RG")
            Contato = Entradados("Digite o Numero de Contato","Contato")
            ArvoreBin.InserirPessoas(Ref0,Nome,Rg,Contato)
        elif operador == "2":
            os.system("cls")
            print("Mostrando Todos as Pessoas Cadastradas:")
            print("")
            ArvoreBin.MostraCad(Ref0,1)
            print()
            os.system("PAUSE")
        elif operador == "3":
            aux = ""
            os.system("cls")
            Busca = ""
            print("Buscando Pessoa Especifica no Cadastro:")
            while aux != "\r":
                aux = msvcrt.getch()
                if aux == "\x08":
                    os.system("cls")
                    aux = len(Busca)-1
                    Busca = Busca[0:aux]
                    pass
                else:
                    Busca = Busca+str(aux)
                    os.system("cls")

                print("Buscando Pessoa Especifica no Cadastro:")
                print("")
                print ("Cadastro com = "),Busca
                print("Mostrando Resultados\n")
                ArvoreBin.MostraCad(Ref0,Busca)
            else:
                os.system("cls")
                print(Busca)
                print("Nao Encontrado")
        elif operador == "4":
            print("Salvando Arquivo")
            f = open("Texto.txt","w")
            f.close()

        elif operador == "5":
            return 0
        else:
            print("VALOR INVALIDO")
            os.system("pause")


principal()



