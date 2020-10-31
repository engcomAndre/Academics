__author__ = 'ANDRE'

import random

def geraLista(numter):
    lista = []

    #for i in range(1,len(lista1)+1):
    lista1 = [1,2,3,4,5,6,7,8,9,0]

    for i in range(0,numter):
        a = random.randint(1,99)*lista1[random.randint(0,len(lista1)-1)]
        lista.append(a)
    print(lista)
    return lista

def GeraListaPar(lista):
    listaP = []
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            listaP.append(lista[i])
    print(30 *"*","\nLista de Numeros Pares:")
    print(sorted(listaP))


def GeraListaImp(lista):
    listaImp = []
    for i in range(0,len(lista)):
        if not (lista[i] % 2 == 0):
            listaImp.append(lista[i])
    print(30 * "*","\nLista de Numeros Impares:")
    print(sorted(listaImp))

def GeraListaPri(lista):
    listaPri = []
    lista = sorted(lista)
    for i in range (0,len(lista)):
        for j in range(0,lista[i]):
            if lista[j] == 0:
                break
            elif not(lista [i] % lista[j] == 0 and j != 0:
                print(lista[i],lista[j])
                listaPri.append(lista[i])
    print(30 * "*","\nLista de Numeros Primos:")
    print(sorted(listaPri))





a = [1,2,3,4,5,6,7]
GeraListaPri(a)
#GeraListaPar(a)
#GeraListaImp(a)

