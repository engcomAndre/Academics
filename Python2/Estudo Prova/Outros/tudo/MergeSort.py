__author__ = 'ANDRE'
import random


def GeraListnum(numter):
    lis = []
    for i in range(0,numter):
        a = random.randint(1,10)
        lis.append(a)
    print (lis)
    return lis


def msort(x):
    lista = []
    if len(x) < 2:
        return x
    medio = int(len(x)/2)
    y = msort(x[:medio])
    z = msort(x[medio:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                lista.append(z[0])
                z.pop(0)
            else:
                lista.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                lista.append(i)
                z.pop(0)
        else:
            for i in y:
                lista.append(i)
                y.pop(0)
    return lista



print(msort(GeraListnum(10)))



