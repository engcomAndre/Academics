#coding:utf8

import os
os.system("clear")

def fib(k):
	a=0
	b=1
	c=a+b
	i=0
	print a,b,
	while i<k:
		print c,
		a=b
		b=c
		c=a+b
		i+=1
k = input("Entre com o valor de truncamento da sequencia: ")
fib(k)
