#-*-coding:cp1252-*-
import random
import glob
import pickle
def geraPessoa():
    lista1 = ['Andre','Cristina','Angelo','Alexandre','Ana Maria','Luis','Carolina','Isabel','Renata','Yasmin']
    lista2 = ['Vieira','da','de','Teixeira','da','de','Luz','Santos','Sales','Tabosa','Almeida','Cristino','Macedo','Oliveira','Maria']
    lista3 = ['Silva','Alberto','Craveiro','Lazaro','Camurca','Gomes','Cirineu','Nazareno','De Luca','Maceio','Novalgino','Mufumba']
    nome1 = lista1[random.randint(0,len(lista1)-1)]
    nome2 = lista2[random.randint(0,len(lista2)-1)]
    nome3 = lista3[random.randint(0,len(lista3)-1)]
    nome = nome1+" "+nome2+" "+nome3
    return nome

def geralista(num_cad):
    Lis_Cad = []
    for i in range(0,num_cad):
        Lis_Cad.append(geraPessoa())
    return Lis_Cad

def imprime_Cad(lista):
    for i in lista:
        print(i)

def salvar_Arq(arq):

    while True:
        for i in glob.glob("*.txt"):
            print(i)
        nome = input("Digite Nome do arquivo:")
        nome_arq = nome+".txt"
        if nome_arq in glob.glob("*.txt"):
            print("********arquivo existente********".upper())
            op = input("Deseja o Adicionar Dados ao Arquivo existente??\nDigite <S> para Sim\nDigite <N> para Não")
            if op  in ["S","s"]:
                f = open(nome_arq,"r")
                lista = f.readlines()
                f.close()
                for i in lista:
                    valor = ""
                    for j in i:
                        if j!= "\n":
                            valor = valor+j
                    arq.append(valor)
                f = open(nome_arq,"w")
                for i in arq:
                    f.write(i+"\n")
                f.close()
            elif op in ["N","n"]:
                print("********arquivo não salvo********".upper())
            else:
                print("*********Valor Inválido**********")
        else:
            f = open(nome_arq,"w")
            for i in arq:
                f.write(i+"\n")
            f.close()
            print("arquivo salvo".upper())
            break



def Abrir_Arq():
    for i in range(0,len(glob.glob("*.txt"))):
        print(i+1,glob.glob("*.txt")[i])
    nome = input("Digite Nome do arquivo:")
    nome_arq = nome+".txt"
    f = open(nome_arq,"r")
    arquivo = f.readlines()
    f.close()
    print (arquivo)
    return arquivo


Abrir_Arq()