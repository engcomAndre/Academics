#coding:utf8

#Este programa retorna o n-ésimo numero da série de fibonacci

import os

os.system("clear")

def fibrec(x):
	
	
	if x<=0:
		return "Erro, entre com valores positivos!!!!"
	elif x==1:
		return 0
	elif x==2:
		return 1
	else:
		return fibrec(x-1)+fibrec(x-2)

x = int(input("Entre com o valor de limitação: "))

print fibrec(x)
