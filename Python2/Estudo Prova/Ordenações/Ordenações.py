__author__ = 'ANDRE'
import random

def geranome(numter):
    lista = []

    #for i in range(1,len(lista1)+1):
    lista1 = [1,2,3,4,5,6,7,8,9,0]

    for i in range(0,numter):
        a = random.randint(1,99)*lista1[random.randint(0,len(lista1)-1)]
        lista.append(a)
    print(lista)
    return lista

def ordLista (lista,key):

    if key == 0:
        a = sorted(lista)
        for i in range (0,len(lista)):
            print("%4d"%(a[i]),end = "")

def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


print(msort(geranome(10)))

