__author__ = 'ANDRE'
###codigo com muitos erros recomaçar quick sort
# programa de classificao por quicksort
#
import os
from datetime import datetime
import random
random.seed()
#
#
os.system("cls")

def quicksort(lista):


    L = []
    R = []
    # caso basico
    if len(lista)<=1:
        return lista
    # calcula a chave
    chave = lista[len(lista)/2]
    #
    for i in lista:
        if i < chave:
            L.append(i)
        if i > chave:
            R.append(i)
        #finaliza
    return quicksort(L)+[chave]+quicksort(R)

# entrada da dados
l = input("Digite o tamanho da lista ")
A = []
i = 0
ing = datetime.now()
while True:
    x = random.randint(1,10*l)
    if x not in A:
        A.append(x)
        i += 1

#    A.append(l-i) # usar essa gerao para testar com valores muito altos
#    i += 1
fig = datetime.now()
ger = fig - ing
inicio = datetime.now()
B = quicksort(A)
fim = datetime.now()
duracao = fim - inicio
print ("-----------")
print ("Original")
print (A)
print ("-----------")
print ("Ordenada ")
print (B)
print ("Tempo (ms) : ","%2.8f"%float(duracao.seconds * 1000 + \
    float(duracao.microseconds)/1000))
print ("Tempo (ms) para gerar a lista : ","%2.8f"%float(ger.seconds * 1000 + \
    float(ger.microseconds)/1000))
