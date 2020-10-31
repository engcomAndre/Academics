#coding:utf8

#Este programa implementa a seguinte sequencia 0,1,3,6,10,15...N
#IDEIA: Note que o programa terá de fazer o seguinte calculo:
# Algarismo da sequencia + sua posição na sequencia EX:

# 0 (posicao 1) proximo (0+1 = 1), segundo = 1 (posição 2)....
# Portanto declarar um contador somar a variável + contador

x = int(input("Entre com a limitação da sequencia:  "))
i=0
y=0
j=0
while j < x:
	j+=1
	print (y) 
	y = y+j
	 
