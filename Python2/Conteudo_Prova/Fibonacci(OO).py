#-*-coding:cp1252-*-
class fibonnaci:
    def __init__(self,num_termos):
        self.num_termos = num_termos
        self.termos_A = 0
        self.termos_B = 1
        self.op = num_termos
        if num_termos <0:
            print("Valor Inválido\nSéries Fibonacci não possuem numero de termos negativo")


    def for_fibonacci(self):
        for i in range(1,self.num_termos):
            print( self.termos_A,end = " ,")
            self.termos_A,self.termos_B = self.termos_B,self.termos_A+self.termos_B
        print(self.termos_A)

    def while_fibonacci(self):
        while self.num_termos > 1:
            self.num_termos -=1
            print(self.termos_A,end = ",")
            self.termos_A,self.termos_B = self.termos_B,self.termos_A+self.termos_B
        print(self.termos_A)

    def rec_fibonacci(self):
        if self.num_termos > 1:
            print(self.termos_A,end = ",")
            self.termos_A,self.termos_B = self.termos_B,self.termos_A+self.termos_B
            self.num_termos-=1
            self.rec_fibonacci()
        elif self.num_termos == 1:
                print(self.termos_A)
        elif self.num_termos == 0:
            print("Serie Fibonacci vazia")


def principal():
    while True:
        try:
            op = int(input("Digite um numero inteiro:"))
            funcao = fibonnaci(op)
            funcao.rec_fibonacci()
        except ValueError:
            print("Valor Inválido\n\nDigite Apenas Números Inteiros")

principal()