__author__ = 'ANDRE'
#Bublesort recursivo
import random
#procedimento que gera massa de teste
def geramassa(numter):
    lista = []
    for i in range (0,numter):
        lista.append(random.randint(0,numter))
    return lista
#Bublesort forma recursiva
def rec_bublesrt(lista):
    for i in range(0,len(lista)-1):
        if lista[i] > lista [i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            rec_bublesrt(lista)
    return lista

x = geramassa(20)
print(x)
print(rec_bublesrt(x))
