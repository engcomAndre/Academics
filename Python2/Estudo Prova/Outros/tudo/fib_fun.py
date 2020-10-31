#coding:utf8

#Definir uma função que gere a série de fibonacci até determinado
#valor "n"
import os
os.system("clear")

def fib(n):
	a,b =0,1
	print a,
	while b<n:
		print b,
		a,b = b, a+b

x = input()

fib(x)
