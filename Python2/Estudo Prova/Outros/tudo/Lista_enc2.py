#encoding:utf8
#qpy:console
#
import math
import os
class Aluno:
   def __init__(self, nome,endereco,email):
      self.nome = nome
      self.endereco = endereco
      self.email = email
   def __str__(self):
      return "\nAluno: "+self.nome+"\nEnd: "+self.endereco+"\ne-mail:"+self.email
# fim da classe
# inicio do programa
lista = []
while True:
	os.system("clear")
	print "Escolha uma opção abaixo:"
	print "<1> Cadastrar um Aluno"
	print "<2> Listar os Alunos " 
	print "<3> Sair do Programa"
	print "<4> Pesquisar por nome "
	print "<5> Atualizar a Lista"
	print "<6> Deletar Nomes"
	escolha = raw_input("Digite sua escolha e pressione <enter> ")
	if escolha == "1":
		os.system("clear")
		nome = raw_input("Digite o nome do aluno ")
		end = raw_input("Digite o endereco do aluno ")
		mail = raw_input("Digite o e-mail do aluno ")
		obj = Aluno(nome,end,mail)
		lista.append(obj)
	elif escolha == "2":
		for i in  lista:
			print i
		raw_input("Digite enter para continuar")
	elif escolha == "3":
		break
	elif escolha == "4":
		nomePesq = raw_input("Digite o nome a pesquisar ")
		for i in lista:
			if i.nome == nomePesq:
				print i
		raw_input("Tecle enter")
print "Fim"
# fim do programa
