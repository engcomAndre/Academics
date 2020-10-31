
import os

class pessoa():

    def __init__(self,nome = "",endereco = "",email = ""):
        self.nome = nome
        self.endereco = endereco
        self.email = email
    def __str__(self):
        return "\nNome: "+self.nome+"\nEnd "+self.endereco+"\nE-mail: "+self.email

def Menu():

    print ("\nEscolha uma opcao abaixo:")
    print ("<1> Cadastrar")
    print ("<2> Listar")
    print ("<3> Localizar")
    print ("<4> Sair do Programa\n")
    return input("Opcao:")

def insiraTermo():
    b = 0
    if b == 0:
        os.system("cls")
        print("Cadastrando Nova Entrada:\n")
        nome = input("Digite o nome  \n ")
        end = input("Digite o endereco\n ")
        email =input("Digite o e-mail\n ")
        b = 1

    op = input("Deseja Inserir?\nDigite S para SIM\nDigite N para Nao")
    while True:
        if op == "S" or op == "s":
            return pessoa(nome,end,email)
        elif op == "N" or op == "n":
            return 0
        else:
            print("Valor Invalido,\nDigite um valor valido")


def principal ():
    primeiro = pessoa()
    atual = primeiro
    ultimo = primeiro
    while True:
        escolha = Menu()
        if escolha == "1":
            os.system("cls")
            objeto = insiraTermo()
            if objeto != 0:
                if primeiro.nome == "":
                    primeiro = objeto
                    ultimo = primeiro
                else:
                    ultimo.proximo = objeto
                    ultimo = ultimo.proximo
                print("Entrada Registrada")
                pass
            else:
                print("Entrada Nao Registrada")



principal()






