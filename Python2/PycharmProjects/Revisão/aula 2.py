__author__ = 'ANDRE'
import os
import math
def quadrado():
    print("Termo inicial:")
    a = int(input())
    print("Numero de Termos")
    numter = int(input())
#    while (numter > 1):
    if numter == 0:
        print("Sequencia sem termos")

    elif numter < 0:
        print("Numero de termos invalido")
    else:
        while numter > 1:
            print(a,end = ", ")
            a = a*a
            numter -= 1
        print(a*a)


def ncom1 ():
    print("Termo inicial:")
    a = int(input())
    b = 0
    print("Numero de Termos")
    numter = int(input())
    while (numter > -1):
        a = a + b
        print(a,end = ", ")
        numter -= 1
        b += 1

def q3 ():
    print("Termo inicial:")
    print("Numero de Termos")
    numter = int(input())
    res = numter
    while numter >= 0:
            res = -res + numter
            if numter == 0 or res == 0:
                print("0",end=", ")
                numter += -1

            else:
                print(numter,end =' e ')
                print(res,end=", ")
                numter+= -1



def menu():
    print("")
    print("1 - Sequencia de Quadrados:")
    print("2 - Sequencia X+(N+1):")
    print("3 - Sequencia sei la:")
    print("0 - Sair:")

    esc = int(input())
    return esc


def principal():
    a = 1
    while a == 1:
        b = menu()
        if b == 1:
            #proc limpa tela
            quadrado()
        elif b  == 2:
            #proc limpa tela
            ncom1()
        elif b  == 3:
            #proc limpa tela
            q3()
        elif b  == 0:
            a = 0
            print("Programa Encerrado")

principal()


