__author__ = 'ANDRE'
import random


def GeraListnum(numter):
    lis = []
    for i in range(0,numter):
        a = random.randint(1,10)
        lis.append(a)
    print (lis)
    return lis

def QuickSort (lista):
    if lista:
        Dir = [x for x in lista if x < lista[0]]
        Esq = [x for x in lista if x > lista[0]]

        if len(Dir) > 1:
            Dir = QuickSort(Dir)
        if len(Esq) > 1:
            Esq = QuickSort(Esq)
        return Dir + [lista[0]*lista.count(lista[0]) + Esq]
    return []

QuickSort(GeraListnum(10))