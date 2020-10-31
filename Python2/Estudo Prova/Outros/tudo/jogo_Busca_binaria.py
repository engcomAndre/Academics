#coding:utf8

#

#Jogo do acerte o numero
#
import random
random.seed()
valor  = random.randint(1,99)
chute = 0
tentativas = 0

while chute != valor:
	chute = int(input("Digite o seu palpite "))
	tentativas+=1
	if chute == valor:
		print ("Parabéns,  você acertou em ",tentativas,"tentativas")
	elif chute < valor:
		print ("Errou para menos na tentativa ",tentativas)
	else:
	 	print ("Errou para mais na tentaiva ",tentativas)


