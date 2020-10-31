__author__ = 'ANDRE'
#encoding:1252
import os
import pickle
import glob
class texto:
    def __init__(self,titulo=None,autor=None,corpo=None):
        self.titulo = titulo
        self.autor = autor
        self.corpo = corpo

def Diretorio():
    return glob.glob("*.txt")

def ListaArquivos(ListaDir):
    print("")
    print(50*"*")
    print("Listando Arquivos do Diretório:")
    print(50*"*")

    for i in range(0,len(ListaDir)):
        nome =""
        for z in range(0,len(ListaDir[i])):
            while ListaDir[i][z] != ".":
                nome = nome+ListaDir[i][z]
                break
            else:
                print("[",i+1,"]",nome)
                break


def AbrirAquivos(lista):
    os.system("cls")
    while True:
        ListaArquivos(lista)
        print("\nEscolha o arquivo que deseja abrir <enter>")
        operador = int(input("Opção"))
        if operador > len(lista):
            print("Arquivo Inexistente\nDigite Valor referente ao arquivo")
            pass
        else:
            arq = open(lista[operador-1],"r")
            for z in arq:
                    print(z,end="")

def CriarArquivos(arq):
    tit = str(arq)
    tit = tit+".txt"


while True:
    print("")
    print(50*"*")
    print(14*" ","PROGRAMA PARA TEXTOS")
    print(50*"*")
    CriarArquivos(texto)
    lista = Diretorio()
    AbrirAquivos(lista)

