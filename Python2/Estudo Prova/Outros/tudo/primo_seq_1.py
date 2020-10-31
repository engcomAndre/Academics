#coding:utf8

#Este programa irá mostrar a sequencia de numeros primos

#Ideia entrar com um numero limite para um efetuar um break.

x = int(input("Digite um valor limite para a sequencia: "))
d=1	#divisores da comparação
y=1	#números que serão divididos para realizar a comparação
i=0	#contador de restos
j=1	#contador da sequência
#Fazer a verificação de números primos e de limite da seq
while j<=x: #limitação da sequência
	
	while d<=y:
		if(y%d==0):
			i+=1
		d+=1
	if(i==2):
		print u"O",j,"\bº número primo é",y
		d=1
		i=0
		j+=1
	else:
		d=1
		i=0
	y+=1
	
	

