#_*_encoding:cp1252_*_
import random
from tkinter import *


class pessoa:
    def __init__(self,nome = "",matricula = "",p1 = 0,p2 = 0):
        self.nome = nome
        self.matricula = matricula
        self.p1 = p1
        self.p2 = p2
        self.n1 = (p1 + p2)/2
        def __str__(self):
            return str(self.nome,self.matricula,self.p1,self.p2,self.n1)





def Menu():
    print("TRABALHO CONCEITOS DE PROGRAMACAO ORIENTADA A OBJETOS\n")
    print(50*"*")
    print ("Escolha o que Deseja Fazer:")
    print ("<0> Adicionar dados(MASSA DE DADOS) ")
    print ("<1> Adicionar dados ")
    print ("<2> Mostrar")
    print ("<3> Pesquisar")
    print ("<4> Apagar/Alterar")
    print ("<5> Resultado Final")
    print ("<6> Salvar")
    print ("<7> Recuperar Arquivo")#não implementado
    print ("<9> Sair")
    a = input("Opção Escolhida mais <<ENTER>>:")
    return a

def geraPessoa(mat):
    lista1 = ['Andre','Cristina','Angelo','Alexandre','Ana Maria','Luis','Carolina','Isabel','Renata','Yasmin']
    lista2 = ['Vieira','da','de','Teixeira','da','de','Luz','Santos','Sales','Tabosa','Almeida','Cristino','Macedo','Oliveira','Maria']
    lista3 = ['Silva','Alberto','Craveiro','Lazaro','Camurca','Gomes','Cirineu','Nazareno','De Luca','Maceio','Novalgino','Mufumba']
    nome1 = lista1[random.randint(0,len(lista1)-1)]
    nome2 = lista2[random.randint(0,len(lista2)-1)]
    nome3 = lista3[random.randint(0,len(lista3)-1)]
    nome = nome1 + " " + nome2+ " " +nome3
    matricula = mat
    fator = 1
    p1 = (random.randint(1,10)/fator)
    p2 = (random.randint(1,10)/fator)
    return pessoa(nome,matricula,p1,p2)

def Procura(lis,termo):
    for i in range(0,len(lis)):
        if termo == lis[i].nome:
            return i
    else:
        return ""





lista = []
def principal():
    while True:
        operador = Menu()
        if operador == "0":
            print("Gerando Teste de Massa")
            quan = input("Digite o numero de pessoas ue deseja gerar e depois tecle <ENTER>:\nQuantidade = ")
            for i in range (0,int(quan)):
                lista.append(geraPessoa(len(lista)+1))
            print("Função Executada com sucesso")

        elif operador == "1":

            print("Cadastrando")
            nome = input("Digite o Nome da Pessoa:\nNome = ")
            matricula = len(lista)+1
            p1 = input("Digite o Nota 1 da Pessoa:\nNota 1 = ")
            p2 = input("Digite o Nota 2 da Pessoa:\nNota 2 = ")
            lista.append(pessoa(nome,matricula,int(p1),int(p2)))

        elif operador == "2":
            print("\n",17*"*","Mostrando Pessoas Cadastradas",16*"*","\n")
            for i in lista:
                print('%-0.7d %-030s %4s    %4s    %4s'%(int(i.matricula),i.nome,i.p1,i.p2,i.n1))

            print("\n",23*"*","Fim de Listagem",23*"*","\n")

        elif operador == "3":
            busca = input("Digite o Termo que Busca e pressionen <ENTER>:")
            operador = Procura(lista,busca)

            if operador == "":
                print("Termo Não Encontrado")
            else:
                print("****************Mostrando Cadastro Localizado:**********\n ")
                print('%-12s %-30s %4s    %4s    %4s'%(lista[operador].matricula,lista[operador].nome,lista[operador].p1,lista[operador].p2,lista[operador].n1))
                print("\n",23*"*","Fim de Listagem",23*"*","\n")

        elif operador == "4":
            busca = input("Digite o Termo que Busca e pressionen <ENTER>:")
            operador = Procura(lista,busca)

            if operador == "":
                print("Termo Não Encontrado")
            else:
                print("****************Mostrando Cadastro Localizado:**********\n ")
                print('%-12s %-30s %4s    %4s    %4s'%(lista[operador].matricula,lista[operador].nome,lista[operador].p1,lista[operador].p2,lista[operador].n1))
                print("\n",23*"*","Fim de Listagem",23*"*","\n")
                op = input("Digite:\n[-1-] Apagar Cadastro\n[-2-]  Alterar\n[-0-] Retornar")
                if op == "1":
                    del (lista[operador])
                elif op == "2":
                    lista[operador].matricula = input("Digite Matrícula:")
                    lista[operador].nome = input("Digite Nome:")
                    lista[operador].p1 = input("Digite Nota 1:")
                    lista[operador].p2 = input("Digite Nota 2:")
                elif op == "0":
                    break
                else:
                    print("Valor Inválido")
        elif operador == "5":
            print("Listando Resultado Final")
            media = 6
            Res1 = "REPROVADO"
            Res2 = "APROVADO"
            for i in lista:
                if i.n1 >= media:
                    print('%-012s %-30s %4s    %4s    %4s  %10s'%(i.matricula,i.nome,i.p1,i.p2,i.n1,Res2))

                else:
                    print('%-012s %-30s %4s    %4s    %4s  %10s'%(i.matricula,i.nome,i.p1,i.p2,i.n1,Res1))
        elif operador == "6":
            nome = ""
            nome = nome+str(input("Digite o nome do arquivo que deseja Criar"))+".txt"
            f = open(nome,"w")
            f.write("")
            for i in lista:
                tex = (str(i.matricula)," ",str(i.nome)," ",str(i.p1)," ",str(i.p2)," ",str(i.n1),"\n")
                f.writelines(tex)
            f.close()



        elif operador == "7":
            #terminar de implementar
            print("Abrindo Arquivo")
            f = open("arquivo.txt","r")
            print(f.readline(-1))



        elif operador == "9":
            print("\n********************Fim de Programa************************")
            break



        else:
            print("VALOR INVALIDO")


principal()