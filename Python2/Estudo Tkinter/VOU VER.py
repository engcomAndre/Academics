#-*-coding:UTF-8-*-
from tkinter import *
root = Tk()

class Janela:

    def __init__(self,principal):
        self.principal  = Frame(principal)
        self.principal["bg"] = "green"
        self.principal.pack(fill = BOTH,expand = YES)

        self.Nome = Label(self.principal)
        self.Nome["text"] = "Texto Qualquer Aqui"
        self.Nome["bg"] = "lightblue"
        self.Nome.pack(fill = BOTH,expand = YES)

        self.Botao = Button(self.principal)
        self.Botao["text"]  = "Texto do botão"
        self.Botao["height"] = 4
        self.Botao["font"] = "Comic Sans MS",15,"italic"
        self.Botao["command"] = self.Janela1
        self.Botao.pack()

    def Janela1(self):

        self.secundaria = Toplevel()
        self.secundaria["bg"] = "red"
        self.secundaria.geometry("300x300+900+300")
        self.secundaria.focus_force()
        self.secundaria.transient(root)
        self.secundaria.grab_set()

        self.Nome = Label(self.secundaria)
        self.Nome["text"] = "Texto caixa 2"
        self.Nome.pack(side = TOP,fill = X,expand = YES)

        self.Botao = Button(self.secundaria)
        self.Botao["command"] = self.Janela2
        self.Botao["text"] = "Botão"
        self.Botao["font"] = "Verdana",15,"bold"
        self.Botao.pack(side = TOP,fill = X,expand = YES)

    def Janela2(self):

        self.secundaria = Toplevel()
        self.secundaria["bg"] = "red"
        self.secundaria.geometry("300x300+900+100")
        self.secundaria.focus_force()
        self.secundaria.transient(root)
        self.secundaria.grab_set()

        self.Nome = Label(self.secundaria)
        self.Nome["text"] = "Texto caixa 2"
        self.Nome.pack(side = TOP,fill = X,expand = YES)

        self.Botao = Button(self.secundaria)
        self.Botao["command"] = self.Fecha
        self.Botao["text"] = "Botão"
        self.Botao["font"] = "Verdana",15,"bold"
        self.Botao.pack(side = TOP,fill = X,expand = YES)















    def Fecha(self):
        self.secundaria.destroy()





Janela(root)
root.mainloop()