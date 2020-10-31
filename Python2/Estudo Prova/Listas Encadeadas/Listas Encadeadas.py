#-*-coding:cp1252-*-
import pickle
import glob





def Abrir_Arq():
    arq = []
    while True:
        print ("Listando Arquivos do Diretorio:")
        for i in range(0,len(glob.glob("*"))):
        #    if ".py" not in glob.glob("*")[i]:
        #        if ".txt" not in glob.glob("*")[i]:
                    print(i+1,"-",glob.glob("*")[i])
                    arq.append(i)
        print("\n\nEscolha o numero do Arquivo que Deseja Abrir:")
        op = int(input("Arquivo Posição:"))-1
        if op > -1 and op in arq:
            f = open(str(glob.glob("*")[op]),"rb")
            lis = pickle.load(f)
            f.close()
            break
        else:
            print("Valor Inválido")
    return lis

def Salvando_Arq(arq):
    while True:
        for i in glob.glob("*.txt"):
            print(i)
        nome = input("Digite Nome do arquivo:")
        nome_arq = str(nome)
        if nome_arq in glob.glob("*"):
            print("********arquivo existente********".upper())
            op = input("Deseja o Adicionar Dados ao Arquivo existente??\nDigite <S> para Sim\nDigite <N> para Não")
            if op  in ["S","s"]:
                f = open(nome_arq,"wb")
                pickle.dump(arq,f)
                f.close()
                break
            elif op in ["N","n"]:
                print("********arquivo não salvo********".upper())
            else:
                print("*********Valor Inválido**********")
        else:
            f = open(nome_arq,"wb")
            pickle.dump(arq,f)
            f.close()
            break


class Aluno:
    Proximo_Aluno = ""
    def __init__(self,Nome = "",Matricula = ""):
        self.Nome = Nome
        self.Matricula = Matricula
    def __str__(self):
        return ("%-0.10d %-12s "%(int(self.Matricula),self.Nome))


def Menu():
    print("\n\nEstudo de Listas Encadeadas:\n".upper())
    print("<0>Cadastrar Massa de Dados")
    print("<1>Cadastrar Novo Aluno")
    print("<2>Mostrar Cadastro")
    print("<3>Pesquisar Aluno")
    print("<4>Alterar/Atualizar")
    print("<5>Excluir Aluno")
    print("<6>Inserção Ordenada")
    print("<7>Fechar Programa")
    try:
        op = int(input("Opção Escolhida"))
        if op in range(0,8):
            return op
        else:
            print("Valor Inválido")
    except ValueError:
        print("Valor Inválido")


#lis_Salvar = [Primeiro,Ultimo,Matricula]
def Main():
#observaçção#comentar essa parte caso o arquivo ainda não tinha sido criado
    lis_Abrir = Abrir_Arq()

    Primeiro = lis_Abrir[0]
    Ultimo = lis_Abrir[1]
    Matricula = lis_Abrir[2]
    #################################################################
#observação ##se o arquivo não tiver sido criado descomentar essa parte
    # Primeiro = Aluno()
    # Ultimo = Primeiro
    # Matricula = 0
    #

    while True:
        op = Menu()
        if op == 0:
#######################################################################

            print(50*"*")
            print("Cadastrando Novo Aluno".upper())
            print(50*"*")
            lis = ["f","l","n","q","t"]
            for i in lis:
                Obj_Aluno = Aluno(i,Matricula)
                if Primeiro.Nome == "":
                    Primeiro = Obj_Aluno
                    Ultimo = Primeiro
                else:
                    Ultimo.Proximo_Aluno = Obj_Aluno
                    Ultimo = Ultimo.Proximo_Aluno
                Matricula += 1

#######################################################################
        elif op == 1:
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
######################################################################################
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
##############################################################################
        elif op == 5:
            print("Excluindo Aluno")
            Locado_Anterior = Primeiro
            Locado = Locado_Anterior.Proximo_Aluno
            Termo_Buscado = input("Digite Termo A Buscar:\nTermo:")

            while Locado_Anterior.Proximo_Aluno != "":
                if Termo_Buscado in [Locado.Nome,Locado_Anterior.Nome]:
                    if Primeiro.Nome == Termo_Buscado:
                        Primeiro = Locado
                        break
                    elif Locado.Nome == Termo_Buscado:
                        Locado_Anterior.Proximo_Aluno = Locado.Proximo_Aluno
                        break
                    elif Locado_Anterior.Proximo == Ultimo:
                        Ultimo = Locado_Anterior
                        break
                    else:
                        break
                else:
                    Locado_Anterior = Locado
                    Locado = Locado.Proximo_Aluno
#######################################################################
        elif op == 6:
            print("Inserção Ordenada")
            Locado_Anterior = Primeiro
            Locado = Locado_Anterior.Proximo_Aluno
            Nome = input("Digite Nome do Aluno:")
            Obj_Aluno = Aluno(Nome,Matricula)
            while Locado.Proximo_Aluno != "":
                if Primeiro.Nome >= Nome:
                    Obj_Aluno.Proximo_Aluno = Primeiro
                    Primeiro = Obj_Aluno
                    break

                elif Locado.Nome >= Nome:
                    Obj_Aluno.Proximo_Aluno = Locado
                    Locado_Anterior.Proximo_Aluno = Obj_Aluno
                    break
                else:
                    Ultimo.Proximo_Aluno = Obj_Aluno
                    Ultimo = Ultimo.Proximo_Aluno
                    break
                Locado_Anterior = Locado
                Locado = Locado_Anterior.Proximo_Aluno
            Matricula+=1
#######################################################################
        elif op == 7:
            print("Fechando Programa")
            lis_Salvar = [Primeiro,Ultimo,Matricula]
            Salvando_Arq(lis_Salvar)
            break
#######################################################################
        else:
            print(50*"*")
            print("Valor Inválido")
            print(50*"*")


Main()


