__author__ = 'ANDRE'
import random
import os
#Gerando Massa de Teste
def geranome(numpal,tampal):
    lista = []
    a = ['q','w','e','r','t','y','u','i','p','a','s','d','f','g','g','j','k','l','z','x','c','v','b','n','m']
    for i in range (0,numpal):
        numletras = random.randint(2,tampal)
        palavras = ""
        while numletras > 0:
            palavras = palavras + a[random.randint(0,len(a)-1)]
            numletras -=1
        lista.append(palavras)
    return lista
#Fim da Massa de Teste


def BuscaCap(lista,termo):
    print(lista)
    for i in range(0,len(lista)):
        for j in range (0,len(lista[i])):
            if lista[i][0] == termo:
                print(lista[i])
                break
            else :
                pass
def menu ():
    print("Digite:")
    print("         < 1 > Para Gerar um nova Lista:")
    print("         < 2 > Buscar Termos nas Lista:")
    print("         < 3 > Para Sair:")
    return int(input("Opcao escolhida:\n"))

def principal ():
    while True:
        op  = menu()
        if op == 1:
            os.system("cls")
            print("Gerando Lista")
            tampalavras = int(input("Digite o Tamanho Maximo das palavras:"))
            quanpalavras = int(input("Digite o numero de palavras da lista:"))
            lista = geranome(quanpalavras,tampalavras)
            print(lista)
        elif op == 2:
            os.system("cls")
            print("Buscando Termos na Lista")
            busca = input("Digite Termo ou iniciais do termo:")
            BuscaCap(lista,busca)
        elif op == 3:
            break
        else:
            print("Valor Invalido")
    print("Fim de Aplicativo")


principal()









