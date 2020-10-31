#-*-coding:UTF-8-*-

class Aluno:
    Proximo_Aluno = ""
    def __init__(self,Nome = "",Matricula = ""):
        self.Nome = Nome
        self.Matricula = Matricula
    def __str__(self):
        return ("%-0.10d %-12s "%(int(self.Matricula),self.Nome))


def Menu():
    print("\n\nEstudo de Listas Encadeadas:\n".upper())
    print("<1>Cadastrar Novo Aluno")
    print("<2>Mostrar Cadastro")
    print("<3>Pesquisar Aluno")
    print("<4>Alterar/Atualizar")
    print("<5>Excluir Aluno")
    print("<6>Fechar Programa")
    try:
        op = int(input("Opção Escolhida"))
        if op in range(1,6):
            return op
        else:
            print("Valor Inválido")
    except ValueError:
        print("Valor Inválido")



def Main():
    Primeiro = Aluno()
    Ultimo = Primeiro
    Matricula = 1
    while True:
        op = Menu()
#######################################################################
        if op == 1:
            print(50*"*")
            print("Cadastrando Novo Aluno".upper())
            print(50*"*")
            Nome = input("Nome do Aluno:")
            Obj_Aluno = Aluno(Nome,Matricula)
            if Primeiro.Nome == "":
                Primeiro = Obj_Aluno
                Ultimo = Primeiro
            else:
                Ultimo.Proximo_Aluno = Obj_Aluno
                Ultimo = Ultimo.Proximo_Aluno
            Matricula += 1


######################################################################
        elif op == 2:
            print("Mostrando Cadastro")
            Locado = Primeiro
            print("%-10s %-12s "%("Matricula","Nome"))
            while True:
                print(Locado)
                if Locado.Proximo_Aluno == "":
                    print("Fim de Cadastro")
                    break
                else:
                    Locado = Locado.Proximo_Aluno
######################################################################

        elif op == 3:
            print("Buscando Aluno\n")
            Locado = Primeiro
            Termo_Buscado = input("Digite Termo A Buscar:\nTermo:")
            print("%-10s %12s "%("Matricula","Nome"))
            contador = 0
            while Locado.Proximo_Aluno != "":
                if Locado.Nome == Termo_Buscado:
                    contador += 1
                    print(Locado)
                    pass
                Locado = Locado.Proximo_Aluno
            else:
                if Ultimo.Nome == Termo_Buscado:
                    contador += 1
                    print(Ultimo)
                    print("Fim da Lista")
                else:
                    print("Fim da Lista")
            print("Encontrados %d registros para o Termo %s"%(contador,Termo_Buscado))
        elif op == 4:
            print("Alterando/Atualizando Registro:")
            Locado = Primeiro
            Termo_Buscado = input("Digite Termo A Buscar:\nTermo:")
            print("%-10s %-12s "%("Matricula","Nome"))
            while True:
                if Locado.Nome == Termo_Buscado:
                    print(Locado)
                    Locado.Nome = input("Digite Novo Nome do Cadastro")
                    print("Registro Alterado")

                else:
                    if Locado.Proximo_Aluno == "":
                        print("Fim de Cadastro")
                        break
                    else:
                        Locado = Locado.Proximo_Aluno

        elif op == 5:
            print("Excluindo Aluno")
            Locado = Primeiro
            Termo_Buscado = input("Digite Termo A Buscar:\nTermo:")
            print("%-10s %-12s "%("Matricula","Nome"))
            while True:
                if Locado.Nome == Termo_Buscado:
                    print("Registro Localizado")
                    print(Locado)
                    op = input("Deseja Excluir Cadastro:\ndigite S para Excluir\nN para Manter:")
                    if op in ["S","s"]:

                    

                else:
                    if Locado.Proximo_Aluno == "":
                        print("Fim de Cadastro")
                        break
                    else:
                        Locado = Locado.Proximo_Aluno


        elif op == 6:
            print("Fechando Programa")
            break

        else:
            print(50*"*")
            print("Valor Inválido")
            print(50*"*")

Main()


