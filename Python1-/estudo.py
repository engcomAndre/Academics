__author__ = 'AEC'
import pickle




def cab():
    print(50*'-')
    print('VEÍCULOS'.rjust(0),end = "")
    print('COR'.rjust(11),end = "")
    print('PLACAS'.rjust(14),end = "")
    print('ANO'.rjust(8))


def mostre(lis):
    print('{0:15s} {1:10s} {2:10s} {3:6s}'.format(lis[0], lis[1], lis[2], lis[3]))


def mostreAll(veiculos):
    cab()
    for i in veiculos:
        mostre(i)


def menu():
    print(50 * '*')
    print('        Este Aplicativo Registra Veículos')
    print(50 * '*')
    print()
    print('DIGITE :')
    print()
    print(' 1 - LISTAR TODOS OS VEÍCULOS')
    print(' 2 - PROCURAR UM VEÍCULO')
    print(' 3 - CADASTRAR UM NOVO UM NOVO VEÍCULO')
    print(' 4 - EXCLUIR UM VEÍCULO')
    return input("              OPÇÃO ESCOLHIDA :")


def principal():
    veiculos = [['gol', 'azul', 'hgg1111', '1555'], ['c3', 'preto', 'fff1111', '1999']]

    while True:
        op = menu()
        if op == '1':
            print('LISTANDO TODOS OS VEÍCULOS CADASTRADOS:')
            mostreAll(veiculos)

        elif op == '3':
            lis = []
            lis.append(input("DIGITE A MODELO DO VEÌCULO:"))
            lis.append(input("DIGITE A COR DO VEÌCULO:"))
            lis.append(input("DIGITE A PLACAS DO VEÌCULO:"))
            lis.append(input("DIGITE A ANO DO VEÌCULO:"))
            veiculos.append(lis)

principal()