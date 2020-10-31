#coding:utf8

#IMplementa a tabuada de multiplicar usando for

import os

os.system("clear")

x =  int(input("Entre com a limitação da tabuada: "))

for i in range(1, x+1):
	for j in range(1,11):
		print i,"X",j,"=",i*j
	print "\n"


