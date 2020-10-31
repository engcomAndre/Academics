#coding:utf8

#fatorial recursivo

import os

os.system("clear")

def fatrec(x):
	if x<0:
		return "ERRO!!!"
	elif x==0:
		return 1
	else:
		return x * fatrec(x-1)

x = int(input("Entre com o numero a fatorar: "))

print "O numero fatorado é: ",fatrec(x)
