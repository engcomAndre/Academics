#-*-coding:cp1252-
from math import *

class F_grau_2:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

        self.delta = pow(b,2)-4*self.a*self.c
        try:
            self.delta_R = sqrt(self.delta)
        except ValueError:
            print("Delta Negativo Função sem raizes Reais")
            principal()

        try:
            self.raiz1 = (-self.b + self.delta_R)/int(2*self.a)
            self.raiz2 = (-self.b - self.delta_R)/int(2*self.a)
        except ZeroDivisionError:
            print("Valor de 'A' igual a zero,função não é de Grau 2")
            principal()
    def res(self):
        return self.raiz1,self.raiz2


def principal():
    while True:
        try:
            print(37*"*")
            print("Calculando Raizes da Função de Grau 2")
            print(37*"*")
            a = int(input("Digite o Valor de 'A'"))
            b = int(input("Digite o Valor de 'B'"))
            c = int(input("Digite o Valor de 'C'"))
            print(37*"*")
            Funcao = F_grau_2(a,b,c)
            res = Funcao.res()
            print(res)
            print(37*"*")
        except ValueError:
            print("Digite Apenas numeros")
            pass

principal()

