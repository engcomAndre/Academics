#-*-coding:cp1252-*-
import random

def imprime_Matriz(matriz):
    for i in matriz:
        print("")
        for z in i:
            print(z,end = " ")

def Matriz_Nula(num_L,num_c):
    M_nula = []
    M_Base = [0]*num_c
    for i in range(0,num_L):
        M_nula.append(M_Base)
    return M_nula



def principal():
    while True:
        nL = int(input("\n\nDigite numero de linhas"))
        nC = int(input("Digite numero de colunas"))
        t = Matriz_Nula(nL,nL)
        imprime_Matriz(t)

principal()