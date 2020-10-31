#encoding:utf8
# nao roda no android
# adaptado de Steven Ferg : Pensando em Tkinter

import os

def handle_A():
    print "Errado, tente de novo!"
    raw_input("Pressione enter para continuar")
def handle_B():
    print "Corretíssimo, trílio é um tipo de flor!"
    raw_input("Pressione enter para continuar")
def handle_C():
    print "Errado! Tente de novo!"
    raw_input("Pressione enter para continuar")
def gera_GUI():
    os.system("clear")
    print "               Jogo Realmente Desafiador "
    print "========================================================"
    print "Pressione a tecla correspondente a resposta e depois tecle enter"
    print " (A). Animal  (B). Vegetal (C). Mineral (X). Sair do programa"
    print "========================================================"
    print "O que é um Trílio?"

if __name__ == "__main__":
    while 1:
        gera_GUI()
        # Observamos o próximo evento
        answer = raw_input().upper()
        # -------------------------------------------------------------- # Ques$
        if answer == "A":
            handle_A()
        elif answer == "B":
            handle_B()
        elif answer == "C":
            handle_C()
        elif answer == "X":
            # limpar a tela e sair do loop principal
            os.system("clear")
            print "bye bye"
            break
        else:
            raw_input("Opção inválida, pressione enter para continuar ")