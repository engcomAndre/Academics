#encoding:utf8
 
from Tkinter import *
 
class Aplicacao:
    def __init__(self, pai):
        self.cesta = Frame(pai)
        self.cesta.pack()
         
        self.botao1 = Button(self.cesta)
        self.botao1["text"] = "Alo rapaziada!"
        #self.botao1.pack()   
        self.botao1.pack(side=LEFT)  
 
        self.botao2 = Button(self.cesta)
        self.botao2.configure(text="texto bobo qualquer")
        #self.botao2.pack()    
        self.botao2.pack(side=LEFT) 
 
        self.botao3 = Button(self.cesta)
        self.botao3.configure(text="Vai entrar nessa?")
        #self.botao3.pack()    
        self.botao3.pack(side=LEFT)     
         
        self.botao4 = Button(self.cesta, text="Adeus!")
        #self.botao4.pack()    
        self.botao4.pack(side=LEFT) 
         
raiz = Tk()
ap = Aplicacao(raiz)
raiz.mainloop()
