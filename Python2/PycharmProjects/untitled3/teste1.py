import os,msvcrt,pickle

# def salvando():
#     lista1 = ['Andre','Cristina','Angelo','Alexandre','Ana Maria','Luis','Carolina','Isabel','Renata','Yasmin']
#     f = open("Texto.txt","w")
#     pickle.dump(lista1,f)
#     f.close()
#
# def abrindo():
#     f = open("Texto.txt","r")
#     for i in f:
#         print(i)
# abrindo()
def imprimecar():
    print("Digite Termo para Imprimir:\n")
    a = msvcrt.getch()
    print("Termo Digitado ="),a
    print(type(a))

while True:
        imprimecar()



