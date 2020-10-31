__author__ = 'ANDRE'
import math
def GeraMatriz(colunas,linhas):
    matrizr = []

    for i in range (0,colunas-1):
        for j in range(0,linhas-1):
            print(i,j)
            matrizr[i][j] = 0
            matrizr.append(matrizr[i][j])
            print(a[i][j])

    return matrizr
a = GeraMatriz(5,5)
def Imprimatriz(matriz):
    for i in range(0,len(matriz)):
        j = 0
        for i in range(o,len(matriz[i])):
            print(matriz[i][j])

