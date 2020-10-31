#coding:utf8

#Imprimir a sequencia 2,4,16,256... até X

x = int(input("Entre com o limte da sequencia: "))
y=2
j=1
while j<=x:
	print y
	flag = y
	y = y * flag		
 	j+=1

