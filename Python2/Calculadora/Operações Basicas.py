#-*-coding:UTF-8-*-
import math

def operacoes(valor1,valor2,operador):
    lisop = ["X","/","+","-"]
    if operador in lisop:
        if operador == lisop[0]:
            return valor1*valor2
        elif operador == lisop[1]:
            return valor1/valor2
        elif operador == lisop[2]:
            return valor1+valor2
        elif operador == lisop[3]:
            return valor1 - valor2
        else:
            print("Valor Inválido")


a = int(input("Digite Valor1"))
b = int(input("Digite Valor2"))
c = input("Digite operador")
d = operacoes(a,b,c)
print(d)





