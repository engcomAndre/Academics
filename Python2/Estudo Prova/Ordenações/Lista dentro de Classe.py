import random

class Numero:
    def __init__(self,n_termos):
        self.Lista = []
        for i in range(0,n_termos):
            self.Lista.append(random.randint(0,100))

    def Saida(self):
        print(self.Lista)
        print(sorted(self.Lista))



a = Numero(5)

a.Saida()
