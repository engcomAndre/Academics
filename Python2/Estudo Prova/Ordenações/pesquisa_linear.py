#coding:utf8

#Encontrar a posição de um elemento em uma lista Pesquisa linear

import os
os.system("clear")

x =  int(input("Entre com o tamanho da lista: "))
l = []

print "Digite os valores da lista: "
for i in range(x):
	l.append(input())

y = int(input("Digite o número que deseja pesquisar na lista: "))

for j in range(x):
	if l[j]==y:
		print "Valor encontrado: ",l[j],"na posição ",j," da lista existente"
	
	elif  j==x-1:
		print "Valor nao encontrado!!!"
