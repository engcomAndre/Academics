#coding:utf8

#Receber um vetor e inverter a ordem dos elementos

import os

os.system("clear")

x = int(input("Digite o tamanho do vetor: "))
l= []
li = []
j=0
for i in range(x):
	l.append(input())

while i>=0:
	
	li.append(l[i])
	i-=1
	j+=1

print "lista original = ",l,"lista invertida  = ",li
		
