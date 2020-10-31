#-*-coding:cp1252*-*-
from tkinter import *
font = "Comic San MS",14,"italic"

class Janela:
    def __init__(self,principal):
        self.principal = principal
        self.Janela1 = Frame(principal)
        self.Janela1.pack(side = TOP,anchor = N,pady = 20,fill = BOTH)

        self.Fun_Nome = Label(self.Janela1)
        self.Fun_Nome["font"] = font
        self.Fun_Nome["text"] = "Fibonnaci".upper()
        self.Fun_Nome["bg"]   = "lightyellow"
        self.Fun_Nome["bd"] = 8
        self.Fun_Nome.pack(anchor = NW,pady = 5,fill = X)


        self.Frame_Dados = Frame()
        self.Frame_Dados.pack(anchor = NW,fill = X)

        self.Dado_In_Nome = Label(self.Frame_Dados)
        self.Dado_In_Nome["font"] = font
        self.Dado_In_Nome["text"] = "ENTRADA"
        self.Dado_In_Nome.pack(side = LEFT,padx = 5,anchor = E,fill = X)

        self.Dado_In = Entry(self.Frame_Dados,relief = SUNKEN)
        self.Dado_In.focus_force()
        self.Dado_In["font"] = font
        self.Dado_In["bd"] = 3
        self.Dado_In["bg"] = "lightgray"
        self.Dado_In.pack(side = TOP,padx = 5)


        self.Botao = Frame()
        self.Botao.pack()
        self.Acao = Button(self.Botao)
        self.Acao["width"] = 15
        self.Acao["text"]  = "ACIONADOR"
        self.Acao["font"]  = font
        self.Acao["bg"] = "lightgreen"
        self.Acao["bd"] = 5
        self.Acao["command"] = self.Fibo
        self.Acao.pack(anchor = S,padx = 5,pady = 45)


        self.Frame_Res_Nome = Frame()
        self.Frame_Res_Nome.pack(side = BOTTOM,fill = BOTH,expand = YES,padx = 10)

        self.res = Label(self.Frame_Res_Nome)
        self.res["text"] = "Resultado"
        self.res["font"] = "Comic San MS",16,"italic"
        self.res.pack()

        self.Nome_Saida_Res = Label(self.Frame_Res_Nome,relief = SUNKEN)
        self.Nome_Saida_Res["text"] = ""
        self.Nome_Saida_Res["bd"] = 3




    def Fibo(self):
        par = self.Dado_In.get()
        if par.isnumeric():
            a = 0
            b = 1
            res = ""
            res = res + str(a)
            for i in range(-1,int(par)):
                if i % 10 == 0 and i > 5:
                    res = res +"\n"
                else:
                    res = res +","+ str(b)

                print(a,end = ",")
                a,b = b,a+b
            self.Nome_Saida_Res["font"] = font
            self.Nome_Saida_Res["text"] = res.rjust(10,"0")
            self.Nome_Saida_Res.pack(anchor = N,padx = 10,pady = 12,fill = BOTH,expand = YES)


        else:
            self.Nome_Saida_Res["fon"] = "Verdana",30,"bold"
            self.Nome_Saida_Res["text"] = "Valor\nInválido"
            self.Nome_Saida_Res.pack(anchor = N,padx = 10,pady = 12,fill = BOTH)



class Janela2:
    def __init__(self,Resultado):
        self.Resultado = Resultado
        self.Resultado = Frame(Resultado)
        self.Resultado.pack(side = TOP,anchor = N,pady = 20,fill = BOTH)


def gerente(par):
        Jan = Tk()
        Jan.title("Entrada de Dados FIBO")
        Jan.minsize(300,300)
        op = Janela(Jan),Janela2(Jan)
        if par == 1:
            print("")

        else:
            Jan1 = Tk()
            Jan1.title("Mostrando Resultados FIBO")
            Jan1.mainloop()




gerente(2)

