# -*- coding: 1252 -*-
import random
import os
import time
import math
#############################################

class Aluno:
   proximo = ""
   def __init__(self, nome="",endereco="",email=""):
      self.nome = nome
      self.endereco = endereco
      self.email = email
   def __str__(self):
      return "\nAluno: "+self.nome+"\nEnd: "+self.endereco+"\ne-mail:"+self.email
# fim da classe
primeiro = Aluno()
atual = primeiro
ultimo = primeiro

# inicio do programa
while True:
    os.system("cls")
    print ("Escolha uma op��o abaixo:")
    print ("<1> Cadastrar um Aluno")
    print ("<2> Listar os Alunos ")
    print ("<3> Buscar ")
    print ("<4> Sair do Programa")
    escolha = input("Digite sua escolha e pressione <enter> ")
    if escolha == "1":
        os.system("cls")
        nome = input("Digite o nome do aluno: ")
        end = input("Digite o endereco do aluno: ")
        mail = input("Digite o e-mail do aluno: ")
        obj = Aluno(nome,end,mail)
        if primeiro.nome == "":
            primeiro = obj
            ultimo = primeiro
        else:
            ultimo.proximo = obj
            ultimo = ultimo.proximo
    elif escolha == "2":
        atual = primeiro
        while True:
            print (atual)
            print ("")
            if atual.proximo == "":
                break
            else:
                atual = atual.proximo
        input("Tecle enter para continuar:  ")
        print ("")

    elif escolha == "3":
        busque = input("Digite o nome do aluno que quer buscar:  ")
        atual = primeiro
        while True:
            if atual.nome == busque:
                print (atual)
                if atual.chave != '':
                    atual = atual.chave
                else:
                    break
            elif atual.proximo == '':
                print ('%s nao encontrado. erro 404.'%busque)
                break
            else:
                atual = atual.proximo

    elif escolha == "4":
        break
print ("Fim")
# fim do programa