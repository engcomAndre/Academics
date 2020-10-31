from random import randint
def geralista(n):
    lista = []
    while n:
        lista.append(randint(0,100))
        n-=1
    return lista

def verifica(lista):
    i = 0 
    while i < len(lista)-1:
        if lista[i] > lista[i+1]:
            print("Não Ordenado")
            return 0
        i+=1
    
    print("Ordenado") 
    return 1           
            


def buble(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def Insertion(lista):
    for i in range(0,len(lista)):
        atual = lista[i]
        j = i - 1
        while(j >= 0 and atual < lista[j]):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = atual
    return lista

def Selection(lista):
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1,len(lista)):
            if(lista[menor] > lista[j]):
                menor = j
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
    
    return lista


def Quick(lista):
    listaMenor = []
    listaPivo = []
    listaMaior = []
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        for i in lista:
            if i > pivo:
                listaMaior.append(i)
            elif i < pivo:
                listaMenor.append(i)
            else:
                listaPivo.append(i)
        listaMenor = Quick(listaMenor)
        listaMaior = Quick(listaMaior)
        return listaMenor + listaPivo + listaMaior 


def Merge(lista):
    listaDireita = []
    listaEsquerda = []
    if len(lista) > 1:
        for i in range(len(lista)):
            if i < len(lista)/2:
                listaEsquerda.append(lista[i])
            else:
                listaDireita.append(lista[i])

        Merge(listaDireita)
        Merge(listaEsquerda)

        i = 0
        j = 0
        k = 0
        while i < len(listaEsquerda) and j < len(listaDireita):
            if listaEsquerda[i] < listaDireita[j]:
                lista[k] = listaEsquerda[i]
                i+=1
            else:
                lista[k] = listaDireita[j]
                j+=1
            k+=1
        while i < len(listaEsquerda):
            lista[k] = listaEsquerda[i]
            i+=1
            k+=1
        while j < len(listaDireita):
            lista[k] = listaDireita[j]
            j+=1
            k+=1

    return(lista)

def Shell(lista):
    intervalo = int(len(lista)/2)
    while intervalo > 0:
        for i in range(len(lista)):
            j = i
            atual = lista[i]
            while j >= intervalo and lista[j - intervalo] > atual:
                lista[j] = lista[j - intervalo]
                j-=intervalo
            lista[j] = atual
        intervalo = int(intervalo/2)
    return(lista)

def Radix(lista):
    lisWork = []
    maxTerInLis = len(str(max(lista)))
    for i in lista:
        zeroNum = str(i)
        zeroNum = str("0" * (maxTerInLis - len(zeroNum)))+ zeroNum
        lisWork.append(zeroNum)
    while maxTerInLis > 0:
        lisBucket = []
        for i in range(len(lisWork)):
            for j in lisWork:
                if int (j[maxTerInLis- 1]) == i:
                    lisBucket.append(j)
        lisWork = lisBucket.copy()
        lisBucket.clear()
        maxTerInLis-=1
        lista.clear()
    for i in lisWork:
        lista.append(int(i))
    return lista

def Bucket(lista):
    listaBucket = []
    for i in range(0,10):
        listaBucket.append([])
    divisor = max(lista)/len(listaBucket)
    if not isinstance(divisor,int):
        divisor = int(divisor)+1
    for i in lista:
        indice = int(i / divisor)
        listaBucket[indice].append(i)
    for i in listaBucket:
        if not i == []:
            for j in range(len(i)):
                for k in range(j+1,len(i)):
                    if i[j] > i[k]:
                        aux = i[j]
                        i[j] = i[k]
                        i[k] = aux
    indice = 0
    while indice < len(lista):
        for i in listaBucket:
            if not i == []:
                for j in i:
                    lista[indice] = j
                    indice+=1
    return lista


def Counting(lista):
    lisWork = []
    lisCount = []
    lisSumCount = []
    for i in range (min(lista),max(lista)+1):
        lisWork.append(i)
    for i in lisWork:
        cont = 0
        for j in lista:
            if i == j:
                cont+=1
        lisCount.append(cont)
    cont = 0
    for i in lisCount:
        cont+=i
        lisSumCount.append(cont)
    lisCount.clear()
    for i in range(max(lisSumCount)):
        lisCount.append(" ")
    while cont :
        for i in range(len(lista)):
            for j in range(len(lisWork)):
                if lista[i] == lisWork[j]:
                    lisCount[lisSumCount[j]-1] = lista[i]
                    lisSumCount[j] = lisSumCount[j]-1
                    cont -=1
    lista.clear()
    lista = lisCount.copy()
    return lista
                
    

  
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Buble")
print("lista :",end =" " )
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(buble(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Insertion")
print("lista :",end =" " )
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Insertion(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Selection")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Selection(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Quick")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Quick(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Merge")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ") 
print(Merge(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Shell")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Shell(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Radix")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Radix(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Bucket")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Bucket(lis),end = " "),verifica(lis)
#######################
lis = [10,10,2,0,7,12,75,9,800,1,7,4,3,5]
#######################
print()
print("Counting")
print("lista :",end =" ")
print(lis,end = " "),verifica(lis)
print("Orden =",end=" ")
print(Counting(lis),end = " "),verifica(lis)



























