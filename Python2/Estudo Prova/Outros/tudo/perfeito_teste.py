#coding:utf8

x = int(input("Entre com o numero de teste:  "))
i=0
j=0
d=1
while d<x:
	if(x%d==0):
		i=d
		j=j+d
	d+=1
if(j==x):
	print x,"é perfeito"
else:
	print x,"não é perfeito"
