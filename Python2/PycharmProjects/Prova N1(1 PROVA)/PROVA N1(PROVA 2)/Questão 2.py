__author__ = 'ANDRE'
#Gera Lista de Numeros Impares
def Impar(ini,fim):
    for i in range(ini,fim):
        if i % 2 == 0:
            print(i+1,end = " ")


def Par(ini,fim,key):
    lisp = []
    lisi = []
    for i in range(ini,fim):
        if i % 2 == 0:
            lisp.append(i)
        else:
            lisi.append(i)
    if key == 0:
        return lisp
    else:
        return lisi


