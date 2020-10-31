#-*-coding:cp1252-*-
from math import *
from random import *

#Calculando as raizes da equaçãode 2 grau
def Raizes_2(a,b,c):
    delta = (b*b)-4*a*c
    try:
        delta_R = sqrt(delta)
    except ValueError:
        print("Delta negativo,função não possue raizes reais.")
        pass
    if delta >= 0:
        try:
            res1 = ((-b + (delta_R))/int(2*a))
            res2 = ((-b - (delta_R))/int(2*a))
            print("Raizes Reais da Função são %3d  e %3d."%(res1,res2))

        except ZeroDivisionError:
            print("A igual a 0,função não é de segundo grau.")
            pass


def principal():
    while True:
        try:
            print(37*"*")
            print("Calculando Raizesda Função de Grau 2")
            print(37*"*")
            a = int(input("Digite o Valor de 'A'"))
            b = int(input("Digite o Valor de 'B'"))
            c = int(input("Digite o Valor de 'C'"))
            print(37*"*")
            Raizes_2(a,b,c)
            print(37*"*")
        except ValueError:
            print("Digite Apenas numeros")
            pass

principal()
