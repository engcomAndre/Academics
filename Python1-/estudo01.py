__author__ = 'AEC'
import pickle
import  random
def geralista ():
    carros


def cab():
    print(50*'-')
    print('VEÍCULOS CADASTRADOS'.rjust(0))
    print(50*'_')
    print('MODELO'.rjust(0),end = "")
    print('COR'.rjust(13),end = "")
    print('PLACAS'.rjust(14),end = "")
    print('ANO'.rjust(8))


def mostre(lis):
    print('{0:15s} {1:10s} {2:10s} {3:6s}'.format(lis[0], lis[1], lis[2], lis[3]))


def mostreAll(veiculos):
    cab()
    for i in veiculos:
        mostre(i)

def busca (veiculos,dl):
    for i in range (len(veiculos)):
            if veiculos[i][0] == dl:
                return i


def menu():
    print()
    print(50 * '*')
    print('        Este Aplicativo Registra Veículos')
    print(50 * '*')
    print()
    print('DIGITE :')
    print()
    print(' 1 - LISTAR TODOS OS VEÍCULOS')
    print(' 2 - PROCURAR UM VEÍCULO')
    print(' 3 - CADASTRAR VEÍCULO')
    print(' 4 - EXCLUIR UM VEÍCULO')
    return input("              OPÇÃO ESCOLHIDA :")




def principal():

    f =open('veículos.arq','rb')
    veiculos = pickle.load(f)
    f.close()
    alter = False
    while True:
            op = menu()
            if op == '1':
                print()
                print('      lISTAR VEÍCULOS : ')
                print(' 1 - POR MODELOS;')
                print(' 2 - POR COR;')
                print(' 3 - POR PLACAS;')
                print(' 4 - POR ANO;')
                op11 = input('ESCOLHA UMA OPÇÃO:')
                if op11 == '1':
                    mostreAll(sorted(veiculos,key = lambda veiculos : veiculos[0]))
                elif op11 == '2':
                    mostreAll(sorted (veiculos,key = lambda veiculos : veiculos [1]))
                elif op11 == '3':
                    mostreAll(sorted (veiculos,key = lambda veiculos : veiculos [2]))
                elif op11 == '4':
                    mostreAll(sorted (veiculos,key = lambda veiculos : veiculos [3]))

            elif op == '2':
                proc = input(('    INSIRA DADOS PARA PESQUISA:').upper())
                re_proc = busca(veiculos,proc)
                if re_proc != int():
                    print()
                    print("             VEÍCULO NÃO ENCONTRADO")
                    print()
                else:
                    cab()
                    mostre(veiculos[re_proc])

            elif op == '3':
                lis = []
                lis.append((input("DIGITE A MODELO DO VEÌCULO:")).upper())
                lis.append(input(("DIGITE A COR DO VEÌCULO:")).upper())
                lis.append(input(("DIGITE A PLACAS DO VEÌCULO:")).upper())
                lis.append(input(("DIGITE A ANO DO VEÌCULO:")).upper())
                veiculos.append(lis)
                print(veiculos)

                alter = True

            elif op == '4':
                proc = (input('INSIRA DADOS PARA PESQUISA:').upper())
                re_proc = busca(veiculos,proc)
                if re_proc != int():
                    print()
                    print("             VEÍCULO NÃO ENCONTRADO")
                    print()
                else:
                    cab()
                    mostre(veiculos[re_proc])
                    opdel = input('DESEJA EXCLUIR O '+proc+' ?:')
                    if opdel == 'S' or 's':
                        del veiculos [re_proc]
                alter = True
            elif op == '0':
                if alter == True:
                    op0 = input('DESEJA SALVAR ALTERAÇÕES?:')
                    if op0 == 'S' or 's' :
                        f = open('veículos.arq','wb')
                        pickle.dump(veiculos,f)
                        f.close()
                        break
                else:
                    break

principal()









