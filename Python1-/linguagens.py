import pickle


def listas():

    a = 0
    lis = []
    nome = ["2","C","COBOL","FORTRAN","JAVA","LISP","LOGO","PYTHON"]
    criador = ["3","Dennis Ritchie","CODASYL","Jonh Backus","James Gosling","Jonh McCarthy","Seymour Papert","Van Rossum"]
    ano = ["3","1972","1960","1957","1995","1959","1968","1991"]
    while a < 8:
        lis.append([nome[a],criador[a],ano[a]])
        a = a + 1
    print(lis)


def menu():
    print("*********************************")
    print("*   Linguagens de Programação   *")
    print("*********************************")
    print("\n  1 - Inserir nova linguagem")
    print("  2 - Buscar linguagem")
    print("  3 - Excluir linguagem")
    print("  4 - Listar linguagens pelo nome")
    print("  5 - Listar linguagens pelo ano")
    print("  0 - Sair do aplicativo")
    return input("\n  Escolha uma opção: ")












