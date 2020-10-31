#coding:utf8

#Este programa verifica se um numero é primo

x =int(input("Digite um valor a ser verificado: "))
i=0
d=1
while d <= x:
	if( x%d == 0):
		i = i+1
	d = d+1
if i == 2:
	print u" É primo!"
else:
	print u" Não é primo!"
	
