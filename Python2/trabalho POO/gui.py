#-*-conding:cp1252-*-
from tkinter import *
font1 = ("Comic San MS",14,"italic","bold")
pad = 8
def  Janela1():
        Janela = Tk()
        Janela.maxsize(280,300)
        Janela.minsize(280,300)
        Janela.geometry("380x350+900+50")
        Janela.title("")


        ##TITULO DO PROGRAMA
        LabelTit = Label(Janela,relief = RAISED)
        LabelTit["text"] = "NOME DO PROGRAMA"
        LabelTit["font"] = font1
        LabelTit["bg"]   = "lightgray"
        LabelTit["fg"]   = "darkgreen"
        LabelTit.grid(row = 1,column = 0,sticky = N+E+S+W,columnspan = 2,padx = pad,pady = 2)

        ProTit = Label(Janela,relief = RIDGE)
        ProTit["text"] = "NOME DO PROCEDIMENTO"
        ProTit["font"] = font1
        ProTit["fg"]   = "darkgreen"
        ProTit.grid(row = 2,column = 0,sticky = N+E+S+W,columnspan = 2,padx = pad,pady = 2)

##FIM TITULO DO PROGRAMA

##INICIO CAIXAS DE ENTRADA DE DADOS
def Janela2():

    EntraDados = Tk()
    EntraDados.maxsize(280,300)
    EntraDados.minsize(280,300)
    EntraDados.geometry("380x350+900+50")

    LabelTitDados = Label(EntraDados,text = "NOVO ALUNO",width = 16,font = font1,relief = SUNKEN)
    LabelTitDados.grid(row = 4,column = 0,columnspan = 3,pady = 25)

    ######################################################
    for i in range(5,8):

        if i == 5:
            widgetnome = "NOME"
        elif i == 6:
            widgetnome = "NOTA1"
        else :
            widgetnome = "NOTA2"

        LabelNome0 = Label(EntraDados,width = 6)
        LabelNome0["text"] = widgetnome
        LabelNome0["font"] = font1
        LabelNome0.grid(row = i,column = 0,padx = 2,pady = 6)

        Nome0 = Entry(EntraDados)
        Nome0.focus_force()
        Nome0["font"] = ("Comic San MS",12,"italic")
        Nome0["bg"] = "lightgray"
        Nome0.grid(row = i,column = 1,padx = 2,pady = 6)

    Confirma = Button(EntraDados,width = 12)
    Confirma["text"] = "INSERIR DADOS"
    Confirma["font"] = font1
    Confirma["bg"]   = "skyblue"
    Confirma.grid(row = 92,column = 0,columnspan = 2,sticky = N+E+S+W,padx = 12,pady = 20)
    ##FIM DAS CAIXA DE ENTRADA DE DADOS

##INICIO CAIXAS DE SAIDA DE DADOS
def Janela3():

    saidadados = Tk()
    saidadados.maxsize(510,300)
    saidadados.minsize(510,300)
    saidadados.geometry("400x300+800+50")
    saidadados["bg"] = "lightgray"
    saidadados.focus_force()



    LabelTitSaidaDados = Label(saidadados,text = "LISTA DE ALUNOS",relief = RAISED,padx = 4)
    LabelTitSaidaDados["font"] = ("Verdana",15,"bold")
    LabelTitSaidaDados["width"] = 40
    LabelTitSaidaDados["bg"] = "lightblue"
    LabelTitSaidaDados.pack()

    for i in range(1,6):
        if i == 1:
            a = 10
            dado = "MATRICULA"
        elif i == 2 :
            a = 35
            dado = "NOME"
        elif i == 3:
            a = 7
            dado = "NOTA 1"
        elif i == 4:
            a = 7
            dado = "NOTA 2"

        else:
            a = 10
            dado = "RESULTADO"

        nome = Label(saidadados,width = a,relief = RIDGE)
        nome["text"] = dado
        nome.pack(side =LEFT,anchor = NW)



def principal(par):
    if par == 1:
        Janela1()
        Janela2()
        Janela3()
    elif par == 2:
        Janela2()
    else:
        Janela3()
    mainloop()



principal(1)