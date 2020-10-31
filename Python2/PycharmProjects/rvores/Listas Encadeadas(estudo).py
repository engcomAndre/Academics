__author__ = 'ANDRE'
import os
class Pessoa:
    chave = ""
    def __init__(self,nome = "",end = "",email = ""):
        self.nome = nome
        self.endereco = end
        self.email = email
    def __str__(self):
        return "\nAluno: "+self.nome+"\nEnd: "+self.endereco+"\ne-mail:"+self.email

def Proc_Cadastrar():
    nome = input("Digite o Nome:")
    end = input("Digite o Endereco")
    email = input("Digite email")
    return Pessoa(nome,end,email)

def menu():
    print(30*"-")
    print("  Estudo de Listas Encadeadas")
    print(30*"-")
    print("Tecle :")
    print("[0]Testando Insercao Ordenada")
    print("[3]Insercao no Inicio")
    print("[4]nsercao fim")
    print("[5]Listar")
    print("[6]Buscar")
    print("[7]Alterar")
    print("[8]Apagar")
    print("[9]Imprimir Ordenando ")

    return input("Opcao")

def Principal ():
    primeiro = Pessoa()
    ultimo = primeiro

    while True:
        operador = menu()
#procedimento de testes:
        if operador == "0":
            print("Testando Inserir Ordenado")
            Objeto = Proc_Cadastrar()
            if primeiro.nome == "":
                primeiro = Objeto
                ultimo = primeiro
            else:
                print("1")
                atual = primeiro
                if Objeto.nome <= atual.nome:
                    if atual == primeiro:
                        Objeto.chave = primeiro
                        primeiro = Objeto


                while atual.chave !="":
                    print("2")
                    if Objeto.nome >= atual.nome:
                        chave_ref = atual
                        atual = atual.chave
                    else:
                        Objeto.chave = atual
                        chave_ref.chave = Objeto



#Insirindo Termos na Lista no inicio
        elif operador == "3":
            Objeto = Proc_Cadastrar()
            Objeto.chave = primeiro
            primeiro = Objeto

#Inserindo Termos na Lista no fim
        elif operador == "4":
            Objeto = Proc_Cadastrar()
            if primeiro.nome == "":
                Objeto.chave = primeiro
                primeiro = Objeto
            else:
                ultimo.chave = Objeto
                ultimo = Objeto

#Imprimindo os elementos presentes na lista
        elif operador == "5":
            if primeiro.nome == "":
                print("Lista Vazia")
                continue
            else:
                atual = primeiro
                while atual != "" and atual.nome != "":
                    print(atual)
                    atual = atual.chave


#Buscando Item dentro da lista
        elif operador == "6":
            parametro_busca = input("Digite o item de busca")
            atual = primeiro
            while atual.chave != "" and atual.nome != parametro_busca:
                atual = atual.chave
            else:
                if atual.nome == parametro_busca:
                    print(atual)
                else:
                    print("Termo Nao Encontrado")


#Alterando Elemento Presente na lista
        elif operador == "7":
            atual = primeiro
            parametro_busca = input("Digite o item de busca")
            while True:
                if atual.nome == parametro_busca:
                    atual.nome =  input("Digite o novo nome")
                    atual.endereco =  input("Digite o novo endereco")
                    atual.email =  input("Digite o novo email")
                    if atual.chave != '':
                        atual = atual.chave
                    else:
                        break
                elif atual.chave == '':
                    print ('%s nao encontrado. erro 404.'%parametro_busca)
                    break
                else:
                    atual = atual.chave

#Deletando Elemento da lista
        elif operador == "8":
            atual = primeiro
            if primeiro.nome == "":
                print("Lista Vazia")
                continue
            parametro_busca = input("Digite o item de busca")
            while atual.nome != parametro_busca:
                chave_ref = atual
                atual = atual.chave
                if atual == "":
                    print("VALOR NAO ENCONTRADO")
                    break
            else:
                if atual == primeiro:
                    if primeiro == ultimo:
                        primeiro = Pessoa()
                        ultimo = primeiro
                    else:
                        primeiro = atual.chave

                elif atual == ultimo:
                    ultimo = chave_ref
                    ultimo.chave = ""
                else:
                    chave_ref.chave = atual.chave
#Printando Lista Ordenada
        elif operador == "9":
            if primeiro == "":
                print("Lista Vazia")
                continue
            atual = primeiro
            menor = primeiro
            while atual != "":
                atual = atual.chave
                if menor.nome <= atual.nome:
                    pass
                else:
                    menor = atual
            else:
                if menor != ultimo:
                    atual = primeiro
                    print(menor)
























Principal()