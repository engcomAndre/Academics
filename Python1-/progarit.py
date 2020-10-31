from Aritmetica import *

def principal():
    while True:
        try:
            print(39*"*")
            print("* Termos de uma Progressão Aritmética *")
            print(39*"*")
            numTer = int(input("\n  Digite o número de termos (zero para sair): "))
            if numTer <= 0:
                break
            terIni = float(input("  Digite o termo inicial: "))
            razao = float(input("  Digite a razão: "))
            print("\n  ",end="")
            progArit(numTer,terIni,razao,5)
            print()
        except(ValueError):
            print("\n  VALOR INVÁLIDO - Favor ... ")

principal()






















