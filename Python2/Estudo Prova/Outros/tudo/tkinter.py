from Tkinter import *
class Aplicacao:
    def __init__(self, pai):
        self.pai = pai
        self.cesta = Frame(pai,padx=30,pady=30,bg="red")
        self.cesta.pack()

        self.botao1 = Button(self.cesta)
        self.botao1.configure(text="OK", background= "green")
        self.botao1.pack(side=LEFT)
        self.botao1.bind("<Button-1>", self.button1Click)

        self.botao2 = Button(self.cesta)
        self.botao2.configure(text="Cancel", background="red")
        self.botao2.pack(side=RIGHT)
        self.botao2.bind("<Button-1>", self.button2Click)
        self.numCliquesB1 = 0


    def button1Click(self, event):
        self.numCliquesB1+=1
        self.botao1.configure(text=str(self.numCliquesB1))


    def button2Click(self, event):
        self.pai.quit()


root = Tk(None,None,"Teste da Janela")
ap = Aplicacao(root)
root.mainloop()