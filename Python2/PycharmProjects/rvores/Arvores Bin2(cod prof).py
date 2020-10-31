__author__ = 'ANDRE'
#encoding:utf8
#qpy:console
#
# arvores binarias
#
import os
os.system("cls")

class Noh:  #definição da classe Nó
    dado,esquerdo,direito = 0,None,None
    def __init__(self, dado):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
    def __str__(self):
        return "{"+str(self.dado)+"}"

# fim da classe Noh

class ArvoreBinaria:                # Definição da classe árvore
    def __init__(self):
        self.raiz = None            # inicializa a raiz
    def criaNoh(self, dado):        # cria um novo noh e o retorna
        return Noh(dado)
    def insere(self, raiz, dado):   # insere um novo dado
        if raiz == None:            # arvore vazia
            return self.criaNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz

    def pesquisa(self, raiz, valor): # Pesquisa um valor na árvore
        if raiz == None:
            return 0
        else:
            if valor == raiz.dado:
                return 1
            else:
                if valor < raiz.dado:
                    return self.pesquisa(raiz.esquerdo, valor)
                else:
                    return self.pesquisa(raiz.direito, valor)

    def imprimirArvore(self, raiz): # imprime a árvore
        if raiz == None:
            pass
        else:
            self.imprimirArvore(raiz.esquerdo)
            print ("{",raiz.dado,"}",
            self.imprimirArvore(raiz.direito))

    def imprimeArvoreInvertida(self, raiz): # imprime a árvore invertida
        if raiz == None:
            pass
        else:
            self.imprimeArvoreInvertida(raiz.direito)
            print ("{",raiz.dado,"}",
            self.imprimeArvoreInvertida(raiz.esquerdo))

    def imprimeNohs(self,raiz):
        if raiz == None: return
        a = raiz.dado
        if raiz.esquerdo != None:
            b = raiz.esquerdo.dado
        else:
            b = None
        if raiz.direito != None:
            c = raiz.direito.dado
        else:
            c = None
        print ("{",a,"[",b,",",c,"]","}",
        self.imprimeNohs(raiz.esquerdo),
        self.imprimeNohs(raiz.direito))

valorRaiz = int(input("Digite o valor raiz da árvore "))
# Cria a árvore binária
ArvoreBin = ArvoreBinaria()
# Adiciona o nó raiz
raiz = ArvoreBin.criaNoh(valorRaiz)
while True:
    os.system("cls")
    print ("Menu da árvore")
    print ("<1> Adicionar dados ")
    print ("<2> Imprimir")
    print ("<3> Pesquisar na árvore")
    print ("<4> Sair")
    resposta = input("\nDigite a sua escolha e pressione ENTER ")
    if resposta == "4":
        break
    elif resposta == "1":
        dado = int(input("Digite o valor a ser adicionado: "))
        # insere valores
        ArvoreBin.insere(raiz, dado)
    elif resposta == "2":
        print ("\nImpressão na forma de lista ",
        ArvoreBin.imprimirArvore(raiz))
        print ("\nImpressão na forma de lista invertida: ",
        ArvoreBin.imprimeArvoreInvertida(raiz))
        print ("\nImpressão por nós : ",
        ArvoreBin.imprimeNohs(raiz))
        input("\nPressione ENTER para continuar ")
    elif resposta =="3":
        dado = int(input("\nDigite um valor para encontrar:  "))
        if ArvoreBin.pesquisa(raiz, dado):
            print ("Encontrado")
        else:
            print ("não encontrado")
        input("\nPressione ENTER para continuar ")

# fim do programa
