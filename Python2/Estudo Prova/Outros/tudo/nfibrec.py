#coding:utf8

#Serie de fib recursiva

import os

os.system("clear")

def fibrec(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else :
		return fibrec(n-1)+fibrec(n-2)
	

n = int(input("Entre com o truncamento da sequencia: "))
i=1
#OBS No lugar do while poderia ser
#for i in range(1,n+1):
#	print fibrec(i),
while i<=n:
	print fibrec(i),
	i+=1
