#-*-coding:UTF-8-*-
from tkinter import *


class Calculadora:
    def __init__(self,principal):
        self.principal = Frame(principal)
        self.principal.pack()

        self.Entrada_Dados = Entry()
        self.Entrada_Dados["bd"] = 3
        self.Entrada_Dados["bg"] = "lightblue"
        self.Entrada_Dados["font"] = ("Verdana",32)
        self.Entrada_Dados.pack(padx = 8,pady = 20)
##########################
##########################
        self.F_Botao = Frame()
        self.F_Botao.pack(anchor = NW,padx = 10)

        self.Botao7 = Button(self.F_Botao)
        self.Botao7["command"] = lambda arg1 = 7:self.MostraValor(arg1)
        self.Botao7["font"] = ("Comic San MS",15)
        self.Botao7["text"] = 7
        self.Botao7["height"] = 2
        self.Botao7["width"] = 5
        self.Botao7.pack(side = LEFT,anchor = N)

        self.Botao8 = Button(self.F_Botao)
        self.Botao8["command"] = lambda arg1 = 8:self.MostraValor(arg1)
        self.Botao8["font"] = ("Comic San MS",15)
        self.Botao8["text"] = 8
        self.Botao8["height"] = 2
        self.Botao8["width"] = 5
        self.Botao8.pack(side = LEFT,anchor = N)

        self.Botao9 = Button(self.F_Botao)
        self.Botao9["command"] = lambda arg1 = 9:self.MostraValor(arg1)
        self.Botao9["font"] = ("Comic San MS",15)
        self.Botao9["text"] = 9
        self.Botao9["height"] = 2
        self.Botao9["width"] = 5
        self.Botao9.pack(side = LEFT,anchor = N)

        self.BotaoD = Button(self.F_Botao)
        self.BotaoD["command"] = lambda arg1 = "/":self.MostraValor(arg1)
        self.BotaoD["font"] = ("Comic San MS",15)
        self.BotaoD["text"] = "/"
        self.BotaoD["height"] = 2
        self.BotaoD["width"] = 5
        self.BotaoD.pack(side = LEFT,anchor = N)
##########################
##########################

        self.F_Botao1 = Frame()
        self.F_Botao1.pack(anchor = NW,padx = 10)

        self.Botao4 = Button(self.F_Botao1)
        self.Botao4["command"] = lambda arg1 = 4:self.MostraValor(arg1)
        self.Botao4["font"] = ("Comic San MS",15)
        self.Botao4["text"] = 4
        self.Botao4["height"] = 2
        self.Botao4["width"] = 5
        self.Botao4.pack(side = LEFT,anchor = N)

        self.Botao5 = Button(self.F_Botao1)
        self.Botao5["command"] = lambda arg1 = 5:self.MostraValor(arg1)
        self.Botao5["font"] = ("Comic San MS",15)
        self.Botao5["text"] = 5
        self.Botao5["height"] = 2
        self.Botao5["width"] = 5
        self.Botao5.pack(side = LEFT,anchor = N)

        self.Botao6 = Button(self.F_Botao1)
        self.Botao6["command"] = lambda arg1 = 6:self.MostraValor(arg1)
        self.Botao6["font"] = ("Comic San MS",15)
        self.Botao6["text"] = 6
        self.Botao6["height"] = 2
        self.Botao6["width"] = 5
        self.Botao6.pack(side = LEFT,anchor = N)

        self.Botao5 = Button(self.F_Botao1)
        self.Botao5["command"] = lambda arg1 = "X":self.MostraValor(arg1)
        self.Botao5["font"] = ("Comic San MS",15)
        self.Botao5["text"] = "X"
        self.Botao5["height"] = 2
        self.Botao5["width"] = 5
        self.Botao5.pack(side = LEFT,anchor = N)
############################
############################
        self.F_Botao2 = Frame()
        self.F_Botao2.pack(anchor = NW,padx = 10)

        self.Botao1 = Button(self.F_Botao2)
        self.Botao1["command"] = lambda arg1 = 1:self.MostraValor(arg1)
        self.Botao1["font"] = ("Comic San MS",15)
        self.Botao1["text"] = 1
        self.Botao1["height"] = 2
        self.Botao1["width"] = 5
        self.Botao1.pack(side = LEFT,anchor = N)

        self.Botao2 = Button(self.F_Botao2)
        self.Botao2["command"] = lambda arg1 = 2:self.MostraValor(arg1)
        self.Botao2["font"] = ("Comic San MS",15)
        self.Botao2["text"] = 2
        self.Botao2["height"] = 2
        self.Botao2["width"] = 5
        self.Botao2.pack(side = LEFT,anchor = N)

        self.Botao3 = Button(self.F_Botao2)
        self.Botao3["command"] = lambda arg1 = 3:self.MostraValor(arg1)
        self.Botao3["font"] = ("Comic San MS",15)
        self.Botao3["text"] = 3
        self.Botao3["height"] = 2
        self.Botao3["width"] = 5
        self.Botao3.pack(side = LEFT,anchor = N)

        self.BotaoM = Button(self.F_Botao2)
        self.BotaoM["command"] = lambda arg1 = "-":self.MostraValor(arg1)
        self.BotaoM["font"] = ("Comic San MS",15)
        self.BotaoM["text"] = "-"
        self.BotaoM["height"] = 2
        self.BotaoM["width"] = 5
        self.BotaoM.pack(side = LEFT,anchor = N)
        ############################
############################
        self.F_Botao2 = Frame()
        self.F_Botao2.pack(anchor = NW,padx = 10)

        self.BotaoP = Button(self.F_Botao2)
        self.BotaoP["command"] = lambda arg1 = ".":self.MostraValor(arg1)
        self.BotaoP["font"] = ("Comic San MS",15)
        self.BotaoP["text"] = "."
        self.BotaoP["height"] = 2
        self.BotaoP["width"] = 5
        self.BotaoP.pack(side = LEFT,anchor = N)

        self.Botao0 = Button(self.F_Botao2)
        self.Botao0["command"] = lambda arg1 = 0:self.MostraValor(arg1)
        self.Botao0["font"] = ("Comic San MS",15)
        self.Botao0["text"] = 0
        self.Botao0["height"] = 2
        self.Botao0["width"] = 5
        self.Botao0.pack(side = LEFT,anchor = N)

        self.BotaoI = Button(self.F_Botao2)
        self.BotaoI["command"] = lambda arg1 = "=":self.MostraValor(arg1)
        self.BotaoI["font"] = ("Comic San MS",15)
        self.BotaoI["text"] = "="
        self.BotaoI["height"] = 2
        self.BotaoI["width"] = 5
        self.BotaoI.pack(side = LEFT,anchor = N)

        self.BotaoA = Button(self.F_Botao2)
        self.BotaoA["command"] = lambda arg1 = "+":self.MostraValor(arg1)
        self.BotaoA["font"] = ("Comic San MS",15)
        self.BotaoA["text"] = "+"
        self.BotaoA["height"] = 2
        self.BotaoA["width"] = 5
        self.BotaoA.pack(side = LEFT,anchor = N)

        self.nome = ""

    def MostraValor(self,valor):
        self.nome = self.nome+str(valor)
        self.Entrada_Dados.insert("0",self.nome)
        print(self.nome)























App = Tk()
Calculadora(App)
App.geometry("280x360+900+50")
App.title("Calculadora")
App["bg"] = "lightgreen"
App.mainloop()
