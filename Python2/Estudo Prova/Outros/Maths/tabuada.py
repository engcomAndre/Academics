#coding:utf8

#Implementar a tabuada de multiplicar
import os
os.system("clear")

x = int(input("Entre com a limitação da tabuada: "))
i=0
j=0
while i<x:
	while j<=10:
		print i," X ",j," = ",i*j
		j+=1
	j=0
	i+=1
	print "\n"
		
