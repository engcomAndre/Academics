#coding:utf8

x =  int(input("Entre com a limitação"))
i=0
j=x
lista = []
while(i<=x):
	#print i
	lista.append(i)
	i+=1
	#print j
	lista.append(j)
	j-=1
	if(i>x and j<0):
		print (lista)


