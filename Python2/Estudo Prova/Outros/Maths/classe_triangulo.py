#coding:utf8

#iniciação a POO

import math
import os
os.system("clear")

class Triangulo:
	c1 = 0
	c2 = 0
	def h(t): # A função deve ter pelo meno um argumento
		return math.sqrt(t.c1**2 + t.c2**2)
##fim da classe
t = Triangulo()
t.c1 = input("Digite o tamanho do cateto 1 ")
t.c2 = input("Digite o tamanho do cateto 2 ")
print "hipotenusa = ",t.h()
