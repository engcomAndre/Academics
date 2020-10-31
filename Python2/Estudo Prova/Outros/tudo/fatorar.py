#coding:utf8

#OBSERVAÇÃO: Quando usamos o return, na função chamamos o print
#Caso contrário se usarmos print na função, na main() chamamos 
#apenas a função!!!!!!!!!!!!!!!!!!

import os
os.system("clear")

def fatorar(x):
	i = x
	k=1
	if x<0:
		return "Erro"
	elif x==0:
		return 1
	else:
		while i>0:
			k = k*i
			i-=1
		return k
x = int(input("Digite o numero a ser fatorado: "))
print fatorar(x)
			
