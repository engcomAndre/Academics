class no:
    dado,esquerdo,direito=0,None,None

    def __init__(s,dado):
        s.esquerdo = None
        s.direito = None
        s.dado = dado

    def __str__(s):
        return "{", str(s.dado), "}"

class arvorebin:
    def __init__(s):
        s.raiz = None

    def criano(s,dado):
        return no(dado)

    def insere(s,raiz,dado):
        if raiz == None:
            return s.criano(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = s.insere(raiz.esquerdo,dado)
            else:
                raiz.direito = s.insere(raiz.direito,dado)
        return raiz

    def imprimearvore(self,raiz):
        if raiz==None:
            pass
        else:
            self.imprimearvore(raiz.esquerdo)
            print("{",raiz.dado,"}", end = "  ")
            self.imprimearvore(raiz.direito)

    def imprimeprimos(s,raiz):
        if raiz == None:
            pass
        else:
            s.imprimeprimos(raiz.esquerdo)
            if checaprimo(raiz.dado) != 0:
                print("{", raiz.dado, "}", end = " ")
            s.imprimeprimos(raiz.direito)

    def imprimeprimosinvertido(self,raiz):
        if raiz==None:
            pass
        else:
            self.imprimeprimosinvertido(raiz.direito)
            if checaprimo(raiz.dado) != 0:
                print("{", raiz.dado, "}", end = " ")
            self.imprimeprimosinvertido(raiz.esquerdo)






def checaprimo(a):
    i = 2
    j = 0
    while i < a:
        if a%i == 0:
            j = j + 1
        i = i + 1

    if j == 0:
        return a

    else:
        return 0




def menu():
    print("\n\n\n")
    print("---------------Menu---------------")
    print("1 - Inserir no")
    print("2 - Imprimir nos primos")
    print("3 - Imprimir nos primos invertido")
    print("4 - Imprimir todos os nos")
    print("0 - SAIR")
    return int(input("\nDigite sua opção: "))



def main():
    x=int(input("Dado raiz da arvore: "))
    arvore=arvorebin()
    raiz=arvore.criano(x)
    p = []

    while(True):
        op=menu()
        if (op==0):
            break

        elif(op==1):
            dado=int(input("\nDigite o valor do no que vai adicionar: "))
            arvore.insere(raiz,dado)

        elif (op==2):
            arvore.imprimeprimos(raiz)

        elif(op==3):
            arvore.imprimeprimosinvertido(raiz)

        elif(op==4):
            arvore.imprimearvore(raiz)

main()