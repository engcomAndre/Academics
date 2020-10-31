__author__ = 'ANDRE'
import math
#Baskara...maior de 3 numeros
def baskara ():
    print("Digite o valor de A:")
    a = int(input())
    print("Digite o valor de B:")
    b = int(input())
    print("Digite o valor de C:")
    c = int(input())

    delta = b*b - (4*a*c)
    if (delta < 0):
        print("Nao existe raiz real.")
    elif (delta == 0):
        print("x = modulo de"-b/2*a)
    else :
        print(delta)
        d = math.sqrt(delta)
        x1 = (-b + d)/2*a
        x2 = (-b - d)/2*a
        print(x1)
        print(x2)

def maior_3 ():
    print("Digite o primeiro valor:")
    a = int(input())
    print("Digite o segundo valor:")
    b = int(input())
    print("Digite o terceiro valor:")
    c = int(input())

    if (a > b):
        if (a > c):
            print(a)
    elif(b > c):
        print(b)
    else:
        print(inc)


def menu():
    print("")
    print("1 - Raiz de funcao quadratica:")
    print("2 - Maior de 3 numeros:")
    print("0 - Sair:")

    esc = int(input())
    return esc


def principal():
    a = 1
    while a == 1:
        b = menu()
        if b == 1:
            #proc limpa tela
            baskara()
        elif b  == 2:
            #proc limpa tela
            maior_3()
        elif b  == 0:
            a = 0
            print("Programa Encerrado")
        else :
            principal("Valor invalido ")
principal()
