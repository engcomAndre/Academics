#coding:utf8

# Desafio. Receber elementos do teclado e adicionar a uma lista.
# Em seguida selecionar o maior e menor valores.

x = int(input("Tamanho da lista: "))
l = []
i=0
flag = 0
maior = 0
menor = 0
j=0
k=0
while i < x:
	print "Digite o valor do elemento l[",i,"]"
	l.append(input())
	i+=1
print "\n Essa é a lista criada ",l
while j<x:
	if l[j]>l[j-1]:
		flag = l[j]
		if maior < flag:
			maior = flag
	j+=1
while k<x:
	if l[k]<l[k-1]:
		flag = l[k]
		if(menor > flag):
			menor = flag
	k+=1
print u"O menor elemento da lista é",menor," e o maior é",maior

	

