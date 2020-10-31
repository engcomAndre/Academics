
#coding:utf8
#
#Este programa soma uma série de números quaisquer.
#

contador = 0
acumulador = 0
quantidade = input("Digite a quantidade de numeros a ser utilizada: ")	#Quantidade de irá truncar o programa
while contador < quantidade:
	numero = input("Digite um valor da série: ")	#Entradas dos numeros de respectiva série
	contador  = contador + 1	#Incremento do contador
	acumulador = acumulador + numero 	#A variável acumulador irá somar todos os numeros da série.
	media = (acumulador)/quantidade	

print u"A soma total da série é: ", acumulador
print u"A média aritmética dos números digitados é: ", media
