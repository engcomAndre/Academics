#coding:utf8

#Implementa uma pesquisa binária

import os

os.system("clear")

def localiza(lista,valor):
	def pesquisa_binaria(min,max):
		if min == max:
			return min
		else:
			meio=(max+min)/2
			if valor>lista[meio]:
				return pesquisa_binaria(meio+1,max)
			else:
				return pesquisa_binaria(min,meio)
	#fim da função interna de pesqusia binaria

	i = pesquisa_binaria(0,len(lista)-1)
	if lista[i]==valor:
		print valor,"encontrado na posição",i
	else:
		print valor,"não encontrado."
#fim da função localiza
l=input("Digite a lista pesquisada: ")
v=input("Qual o valor a pesquisar? ")

localiza(l,v)

#fim do programa
