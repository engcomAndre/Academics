#-*- encoding:cp1252-*-

from tkinter import *
class Janela:

    def __init__(self,toplevel):
        self.label = Frame(toplevel)
        self.label.pack()
        self.label1 = Frame(toplevel)
        self.label1.pack()
        self.entry = Frame(toplevel)
        self.entry.pack()
        self.botao = Frame(toplevel)
        self.botao.pack()
        self.label2 = Frame(toplevel)
        self.label2.pack()



        font = ("Verdana","14","bold",)

        self.label = Label(self.label,fg = "red",text = "Principal",font = font)
        self.label.pack()
        self.label1 = Label(self.entry,font = font,text = "     Digite o Nome   ")
        self.label1.pack(side = LEFT)

        self.nome = Entry(self.entry,width = 12,font = font,bg = "yellow")
        self.nome.focus_force()
        self.nome.pack(side = LEFT)

        self.botao = Button(self.botao,text = "   OK    ",fg = "green",font = font,command = self.tes_botao)
        self.botao.focus_force()
        self.botao.pack()

        self.label2 = Label(self.label2,font = font,text = "esperando")
        self.label2.pack()



    def tes_botao(self):
        self.label2["text"] = "teste ok"











raiz = Tk()
Janela(raiz)
raiz.mainloop()


