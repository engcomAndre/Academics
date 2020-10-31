#coding:utf8
#
#Este programa irá imprimir uma série com x valores primos
#

x = int(input("Digite a quantidade de números que a série deve conter: "))
i=0
j=0
d=1
y=1
while j < x:
	r = y%d
	if r == 0:
		i = i + 1
	if i == 2:
		j = j + 1
		print y
		i = 0
		d = 1
		y+=1
	if d == y:
		d = 1
		y = y + 1
	else:
		d = d+1	


