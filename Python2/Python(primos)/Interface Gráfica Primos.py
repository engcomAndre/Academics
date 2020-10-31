#-*-coding:UTF-8-*-
from Tkinter import *
a = Tk()
a.title("Testador de Primos")
a.geometry("500x200+900+50")
a.maxsize(500,200)
a.minsize(500,200)

Tit_Mostrador = Label(a)
Tit_Mostrador["text"] = "Testa se um Número é Primo"
Tit_Mostrador["font"] = "Verdana",11,"bold"
Tit_Mostrador.pack(anchor = N,pady = 5)

Lab_Numero = Label(a)
Lab_Numero["text"] = "Digite Numero que Deseja Testar"
Lab_Numero["font"] = "Calibri",13,"italic"
Lab_Numero.pack(anchor = N,pady = 5)

def geraprimo ():
    termo = Numero.get()
    if termo.isnumeric():
        termo = int(termo)
        if termo in [0,1]:
            Mostrador["bg"] = "lightyellow"
            Mostrador["text"] = ("O número %d não é primo"%(termo))
            Mostrador.pack(anchor = N,pady = 5)
        elif termo % 2 == 0 and termo == 2:
            Mostrador["bg"] = "lightblue"
            Mostrador["text"] =("O número %d é primo"%(termo))
            Mostrador.pack(anchor = N,pady = 5,fill = X,padx = 12)
        elif termo % 2 == 0 and termo >2:
            Mostrador["bg"] = "lightyellow"
            Mostrador["text"] = ("O número %d não é primo,é divisivel por %d"%(termo,2))
            Mostrador.pack(anchor = N,pady = 5,fill = X,padx = 12)
        else:
            for i in range(3,termo+1,2):
                if termo % i == 0:
                    if i == termo:
                        Mostrador["bg"] = "lightblue"
                        Mostrador["text"] =("O número %d é primo"%(termo))
                        Mostrador.pack(anchor = N,pady = 5,fill = X,padx = 12)
                    else:

                        Mostrador["bg"] = "lightyellow"
                        Mostrador["text"] = ("O número %d não é primo,é divisivel por %d"%(termo,i))
                        Mostrador.pack(anchor = N,pady = 5,padx = 12)
    else:
        Mostrador["bg"] = "red"
        Mostrador["text"] = ("O termo "+termo+" não é número digite somente numeros")
        Mostrador.pack(anchor = N,pady = 5,padx = 12,fill = X,expand = YES)


def geraprimo_a(e):
    geraprimo()

Numero = Entry(a,font = ("Verdana",14,"italic"))
Numero["width"] = 4
Numero.focus_force()
Numero.bind("<Return>",geraprimo_a)
Numero.pack()

Acao = Button(a,command = geraprimo)
Acao["text"] = "AVALIAR"
Acao["font"] = "Verdana",12,"bold"
Acao["width"] = 17
Acao["bd"] = 5

Acao.pack(anchor = N,pady =5)
Mostrador = Label(a,fg = "black",relief = SUNKEN)
Mostrador["width"] = 20
Mostrador["bd"] = 5
Mostrador["font"] = "Comic San MS",16,"italic"
Mostrador["bg"] = "green"

a.mainloop()

