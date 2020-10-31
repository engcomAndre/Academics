__author__ = 'AEC'

def fatorial ():


        res = 1
        num = menu()
        print (num,end="! = ")
        for i in range(num,1,-1):
            print (i,end=" X ")
            res = i * res
        print("1",end = " = ")
        print(res)




def menu():
    print(49*"*")
    print("* Esse Programa Calcula O Fatorial de um Número *" )
    print(49*"*")
    print("")
    return input(" DIGITE UM NÚMERO INTEIRO <ENTER PARA SAIR:>")


def principal():
    while True:
        res = 1
        num = menu()
        if num =="":
            break

        else:
            try:
                num1 = int(num)
            except ValueError:
                print('                 Valor Inválido\n')
                print('Por Favor Digite um Número Inteiro Maior ou Igual a "0"')
                principal()
            if num1 == 1:
                print ("1! = 1")
            elif num1 < 0:
                print('                 Valor Inválido\n')
                print('Por Favor Digite um Número Inteiro Maior ou Igual a "0"')
            elif num1 == 1:
                print ("0! = 1")
            elif num1 == 0:
                print("0! = 1")
            else:
                print (num1,end="! = ")
                for i in range(num1,1,-1):
                    print (i,end=" X ")
                    res = i * res
                print("1",end = " = ")
                print(res)


principal()




