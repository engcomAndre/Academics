#coding:utf8

x = int(input("Digite o limite da sequencia:  "))
i=0
d=1
j=0
y=1
k=0
while k<x:
	while d<y:
		if(y%d==0):
			i=d + i
		d+=1
	if(i==y):
		k+=1
		print ("O",k,"\bº numero perfeito é ",y)
		i=0
		d=1
		y+=1
	else:
		d=1
		i=0
	y+=1
