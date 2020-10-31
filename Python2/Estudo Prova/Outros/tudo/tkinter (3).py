from Tkinter import *
raiz = Tk()
cesta = Frame(raiz)
cesta.pack()
botao = Button(cesta)
botao["text"]= "Ola rapaziada"
botao["background"]= "red"
botao.pack()
raiz.mainloop()