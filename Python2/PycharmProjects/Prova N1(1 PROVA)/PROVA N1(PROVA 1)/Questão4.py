__author__ = 'ANDRE'
import math

def seriafib(numter):
    x = 0
    lis = []
    for i in range(0,numter):
        if i <= 1:
            lis.append(i)
        else:
            lis.append(lis[i-1]+lis[i-2])
    for i in range(0,len(lis)):
        x = x + lis[i]
    print(lis)

    print(x)


seriafib(8)