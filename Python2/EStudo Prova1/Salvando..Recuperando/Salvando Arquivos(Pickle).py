#-*-coding:cp1252-*-
import glob
import pickle



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
            break
        else:
            print("Valor Inválido")
    return f



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
                f = open(nome_arq,"rb")
                arquivo = pickle.load(f)
                f.close()
                f = open(nome_arq,"wb")
                pickle.dump(arq,arquivo)
                pickle.dump(arquivo,f)
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

def Menu():
    print("<1>Para Abrir Arquivo")
    print("<2>Salvar Arquivo")
    print("<3>Imprimir Dados")
    return input("Digite a opção que deseja acessar:")

def principal():

    while True:
        op = int(Menu())
        if op == 1:
            Dados = Abrir_Arq()
        elif op == 2:
            Salvando_Arq(Dados)
        elif op == 3:
            for i in Dados:
                print(i)
        else:
            print("Valor inválido")

principal()

