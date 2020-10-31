#coding:utf8

import os
os.system("clear")

#definindo a função fatorial

def fat(n):
	if n<0:
		return "Erro não existe fatorial de numero negativo"
	elif n == 0:
		return 1
	else:
		fat = n
		for i in range(1,n):
			fat = fat * i
		return fat
n = input()
print fat(n)
#fim da função
