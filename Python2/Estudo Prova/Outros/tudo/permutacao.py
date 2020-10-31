#coding:utf8

import os
os.system("clear")

def permutacao(a,b):
	if len(a) == 0:	return len(b) == 0
	if a[0] in b:
		i = b.index(a[0])
		return permutacao(a[1:],b[0:i]+b[i+1:])
	return False

A = input("Lista 1: ")
B = input("Lista 2: ")
print (permutacao(A,B))



