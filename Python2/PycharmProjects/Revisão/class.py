__author__ = 'ANDRE'
import os

class Aluno:
    proximo = ""
    def __init__(self, nome="",endereco="",email=""):
        self.nome = nome
        self.endereco = endereco
        self.email = email
    def __str__(self):
        return "\nAluno: "+self.nome+"\nEnd: "+self.endereco+"\nE-mail: "+self.email

# fim da classe
primeiro = Aluno()
atual = primeiro
ultimo = primeiro

# inicio do programa
while True:
	os.system("cls")
	print ("Escolha uma opcao abaixo:")
	print ("<1> Cadastrar um Aluno")
	print ("<2> Listar os Alunos ")
	print ("<3> Localizar Termo")
	print ("<4> Sair do Programa")

	escolha = input("Digite sua escolha e pressione <enter> ")
	print(escolha)
	if escolha == "1":
		os.system("cls")
		nome = input("Digite o nome do aluno \n ")
		end = input("Digite o endereco do aluno\n ")
		email =input("Digite o e-mail do aluno\n ")
		obj = pessoa(nome,end,email)
		if primeiro.nome == "":
			primeiro = obj
			ultimo = primeiro
		else:
			ultimo.proximo = obj
			ultimo = ultimo.proximo
	elif escolha == "2":
		atual = primeiro
		while True:
			print(atual)
			if atual.proximo == "":
				break
			else:
				atual = atual.proximo
	elif escolha == "3":
		atual = primeiro
		busca = (input("Digite  Termo:"))
		for i in atual(0,len(obj)):
			if atual.nome == busca:
				print(atual.nome)
		while True:
			if atual.nome == busca:
				print(atual)
				break
				pass
			elif not(atual.nome == ""):
				atual = atual.proximo
				break
			elif atual.proximo == "":
				print("Termo nao encontrado")
				break
	elif escolha == "4":
		break
	input("Tecle enter para continuar ")

print ("Fim")

