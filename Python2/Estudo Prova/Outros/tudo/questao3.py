x=int(input("Tamanho da lista: "))

l = []
produto = 1 
i=0
restos=0
div=1
j=0

while i < x:
	print ("Digite o valor do elemento l[",i,"]")
	l.append(input())
	i+=1
print (l)

while(j<x):
	
	while (div <= l[j]):
		if(l[j]%div==0):
			restos+=1
		div+=1
	if(restos==2):
		produto = produto*l[j]
		div=1
		restos=0
	else:
		div=1
		restos=0
	j+=1
		
print ("Produto = ",produto)
