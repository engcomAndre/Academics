#coding:utf8

x=int(input("Tamanho da lista: "))

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
while j>l[j-1]:
	flag = l[j]
	if maior < flag:
		maior = flag
	j+=1

	while k<x:
		if l[k] flag):
		menor = flag
	k+=1
print "O menor elemento da lista é",menor," e o maior é",maior
