__author__ = 'LMC2'
import pickle
import random


def menu ():
    print(29*"*")
    print("* Tradutor Inglês-Português *")
    print(29*"*")
    print()
    print('1 - Buscar termo')
    print('2 - Introduzir novo termo')
    print('3 - Alterar Termo')
    print('4 - Remover Termo')
    print('5 - Listar termos em inglês')
    print('6 - Listar termos em português')
    print('0 - Sair')
    print()
    return (input('Escolha uma opção:'))


def mostre1 (lisp,lisi):
    print('{0:15s} {1:15s}'.format(lisp[0],lisi[0]))

def mostreAll1(lisp,lisi):
    for i in range(len(lisp)):
        mostre1(lisp,lisi)

def mostre2(lisp,lisi):
        print('{0:15s} {1:15s}'.format(lisi[0],lisp[0]))

def buscar(lisi,termo):
    for i in range (len(lisi)):
        if lisi[i] == termo:
            return i

def buscar2(lisi,termo):
    for i in range (len(lisi)):
        if lisi[i] == termo:
            return True


def principal():

    f = open('prova1.arq','rb')
    lisp = pickle.load(f)
    f.close()
    f1 = open('prova2.arq','rb')
    lisi = pickle.load(f1)
    f1.close()
    print(lisi)
    print(lisp)

    while True:

        op = menu()
        if op == '0':
            f = open('prova1.arq','wb')
            pickle.dump(lisp,f)
            f.close()
            f1 = open('prova2.arq','wb')
            pickle.dump(lisi,f1)
            f1.close()
            break



        elif op == '1':
            print()
            print(19*'*')
            print('* Buscar palavra *')
            print(19*'*')
            op1 = (input('Termo em inglês:').lower())
            opr1 = buscar(lisi,op1)
            print('{0:15s} {1:15s}'.format(lisi[opr1],lisp[opr1]))

        elif op == '2':
            print()
            print(22*'*')
            print('* Inserir novo termo *')
            print(22*'*')
            op2 = (input('Termo em inglês:').lower())

            if buscar2(lisi,op2) == True:
                print('Termo já existe')
            else:
                lisi.append(op2)
                lisp.append(input('Termo em português:').lower())


        elif op == '4':
            print()
            print(19*'*')
            print('* Remover palavra *')
            print(19*'*')
            op4 = (input('Termo em inglês:').lower())
            opr4 = buscar(lisi,op4)
            del (lisi[opr4])
            del (lisp[opr4])


        elif op == '5':
            for i in range (len (lisp)):
                print('{0:15s} {1:15s}'.format(lisi[i],lisp[i]))


        elif  op == '6':
            for i in range (len (lisp)):
                print('{0:15s} {1:15s}'.format(lisp[i],lisi[i]))


principal()



