#encoding:utf8
#qpy:console
#
# Inicidando a POO
#
import math
import os
os.system("clear")
class Triangulo:
	c1=0
	c2=0
	def __ini__(self):
		self.c1 = input("Digite o tamanho do cateto 1 ")
		self.c2 = input("Digite o tamanho do cateto 2 ")
	def h(self): #A função deve ter pelo menos um argumento
		return math.sqrt(self.c1**2 + self.c2**2)
# fim da classe
t = Triangulo()
print u"Hipotenusa é ",t.h()
