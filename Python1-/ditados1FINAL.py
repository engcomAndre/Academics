__author__ = 'AEC'
import random

def lis():
    ditados = ["Em terra de cego quem tem um olho é caolho !!!", "Quem espera, senta e cansa.", "Escreveu não leu ... analfabeto." ,"Quem ri por último ... ri atrasado ou não entendeu a piada!", "A união faz .... o açúcar","Em rio que tem piranha jacaré usa camisinha !!!","Devagar ... chega-se atrasado.","Quem cedo madruga, não pega ônibus lotado!","Deus iscrévi sértu... mas eu não!", "Quem é vivo, sempre aparece... nas horas mais impróprias!","Prevenir é melhor que... ser pego de surpresa!","Desgraça pouca é bobagem... é bobagem!","Cautela e caldo de galinha não faz mal à ninguém... exceto à galinha!",
"Quem dá aos mnuamanuapobres... adeus!","Em rio que tem piranha... leve camisinha!"]
    return ditados

def menu():
    print(21*"=")
    print("= Ditados Populares =")
    print(21*"=")
    print("\n")
    print("  1 - Mostrar Próximo Ditado")
    print("  2 - Mostrar um Ditado Aleatório")
    print("  3 - Novo Ditado")
    print("  0 - Sair")
    return input("\n  ESCOLHA UMA OPÇÃO: ")

def principal():
    a = lis()
    cont = 0
    while True:
        cn = menu()
        if cn == "1":
            if cont == len(a):
                    cont = 0
            print("\n\n")
            print (a[cont])
            print("\n\n")
            cont = cont + 1
        elif cn == "2":
            print("\n\n")
            print(random.choice(a))
            print("\n\n")
        elif cn == "3":
            a.append(input ("DIGITE UM NOVO DITADO:\n"))
        elif cn == "0":
            print("FIM DE APLICATIVO")
            break
        else:
            print("\n  OPÇÃO INVÁLIDA\n")
            print("\n\nPOR FAVOR,INSIRA UM VALOR VÁLIDO")
principal()















