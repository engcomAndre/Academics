#coding:utf8

#Selecionar os elementos pares de um vetor:

import os
os.system("clear")

x = int(input("Entre com o tamanho do vetor: "))
v = []
vp = []
print "Digite agora as componentes do vetor: "
for i in range(x):
	v.append(float(input()))
print v
for j in range(x):
	if v[j]%2==0:
		vp.append(v[j])

if len(vp)!=0:
	print "O vetor com numeros pares é: ",vp
else:
	print "Não foram digitados números pares no vetor!!!!"		
