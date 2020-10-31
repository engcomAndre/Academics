#encoding:utf8
#qpy:console
#
# Ini Poo
#
import math
import os
os.system("clear")
class Triangulo:
	area = 0
	tipo = " "
	def __init__(self):
		print "Criada a classe base"
class TrianguloRetangulo(Triangulo):
	l1 = 0
	l2 = 0
	def __init__(self):
		Triangulo.__init__(self)
		print "Criando a classe derivada"
		self.l1 = input("Qual o valor do lado 1 ")
		self.l2 = input("Qual o valor do lado 2 ")
		self.area = self.l1*self.l2/2.0
		print "Área = ",self.area
	def h(self):
		return math.sqrt(self.l1**2 + self.l2**2)
#fim da classe

#Inicio do programa principal
t = Triangulo()
tr = TrianguloRetangulo()
t = tr
#chamada polimorfica
print "Hipotenusa (Usando t) ",t.h()
print "Hipotenusa (Usando tr) ",tr.h()
t.l1 = 1000
print "l1 em t é ",t.l1
print "l1 em tr é ", tr.l1
