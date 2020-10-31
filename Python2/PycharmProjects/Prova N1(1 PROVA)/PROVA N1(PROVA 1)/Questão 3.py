__author__ = 'ANDRE'
import  random

#Produto de Matrizes
def geraMnula(nlin,ncol):
    matrizr = []
    for i in range (1,ncol):
        matriz = [random.randint(1,9)]
        matriz.append(matriz[0])
    for j in range (0,nlin):
        matrizr.append(matriz)
    return matrizr

def prodmatrizes(A,B):
    nlA = len(A)
    ncA = len(A[0])
    nlB = len(B)
    ncB = len(B[0])
    if ncA!=nlB:
        return 0
        C = geraMnula(nlA,ncB)
        for i in range(0,nlA):
            for j in range(0,ncB):
                valor = 0
                for k in range(0,ncA):
                    valor = valor + A[i][k]*B[k][j]
                    C[i][j]=valor


        for i in C(0,len(C)):
            print(i)

x = geraMnula(2,3)
y = geraMnula(4,5)
prodmatrizes(x,y)

