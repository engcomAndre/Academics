__author__ = 'ANDRE'
coding = 1258

import random
random.seed()
def enterlis():
    lis = []
    while True:
        a = input("Digite termos\n")
        lis.append(a)
        a = sorted(lis)
        print(a)


def geranome():
    lista = []
    lista1 = ['Andre','Cristina','Angelo','Alexandre','Ana Maria','Luis','Carolina','Isabel','Renata','Yasmin']
    lista2 = ['Vieira','da','de','Teixeira','da','de','Luz','Santos','Sales','Tabosa','Almeida','Cristino','Macedo','Oliveira','Maria']
    lista3 = ['Silva','Alberto','Craveiro','Lazaro','Camurca','Gomes','Cirineu','Nazareno','De Luca','Maceio','Novalgino','Mufumba']
    #for i in range(1,len(lista1)+1):
    nome1 = lista1[random.randint(0,len(lista1)-1)]
    nome2 = lista2[random.randint(0,len(lista2)-1)]
    nome3 = lista3[random.randint(0,len(lista3)-1)]
    nomef = nome1 + " " + nome2+ " " +nome3

    return nomef

def geradate ():
    ano = random.randint(1920,2015)
    mes = random.randint(1,12)
    if ano % 4 == 0 and mes == 2:
        dia = random.randint(1,29)
    elif ano % 4 != 0 and mes == 2:
        dia = random.randint(1,28)
    elif mes in [1,3,5,7,8,10,12]:
        dia = random.randint(1,31)
    else:
        dia = random.randint(1,30)
    data = [dia, mes, ano]
    return data

def geranumRg():
    return random.randint(0000000000,9999999999)

def geraCpf ():
    return random.randint(00000000000,99999999999)



def geraCad():
    cad = []
    cad.append(geranome())
    cad.append(geradate())
    cad.append(geranumRg())
    cad.append(geraCpf())
#    print(cad)
    return cad



def geraLisCad (numCad):
    lisCad = []
    for i in range(0,numCad):
        a = geraCad()
        lisCad.append(a)
    return lisCad

def OrdLis(lis,key):
    if key == 1:
        return sorted(lis,key = lambda  lis: lis[key][2])
    else:
        return sorted(lis,key = lambda  lis: lis[key])



#print("%d : %d : %d" %(hor,min,seg))

def ImpreLis (a):
    #a = geraLisCad(5)
    #print(a)
    print(" ",85*"-"," ")
    print("|%25s %14s  |%9s |%10s %3s |%10s %4s| "%('Nome',"",' Data Nasc ','Rg',"",'CPF',""))
    print("|",85*"-","|")
    for i in range(0,len(a)):
        print("|%3d | %-35s | %02d/%02d/%4d | %13d | %013d |  "%(i+1,a[i][0],a[i][1][0],a[i][1][1],a[i][1][2],a[i][2],a[i][3]))
    print("|",85*"-","|")



def menu ():
    print('\n\nPrograma Basico de Cadastro de Pessoas\n\n----------MENU PRINCIPAL----------\n\nDIGITE :\n')
    print("[ -1- ] Mostrar Cadastro")
    print("[ -2- ] Procurar Cadastro")
    print("[ -3- ] Editar Cadastro")
    print("[ -4- ] Novo Cadastro")
    return int(input('OPCAO'))

def MenuImpLis ():
    print("Escolha como deseja a Ordenacao:\n\nDigite:")
    print("[ -0- ] Voltar ao Menu Principal")
    print("[ -1- ] Ordenada por Nome")
    print("[ -2- ] Ordenada por Data de Nascimento")
    print("[ -3- ] Ordenada por Rg")
    print("[ -4- ] Ordenada por CPF")
    return int(input("OPCAO:"))

def EnconTer ():
    a = geraLisCad(5)
    print(a)
    ter = input('Termo:')
    for i in range(0,len(a)):
        for j in range(0,len(a[i-1])):
            if j == 1:
                for h in range(0,len(a[i][1])):
                    print(i,j,h)
                    if int(ter) == a[i][1][h]:
                        print(" ",85*"-"," ")
                        print("|",85*"-","|")
                        print("|%25s %14s  |%9s |%10s %3s |%10s %4s| "%('Nome',"",' Data Nasc ','Rg',"",'CPF',""))
                        print("|",85*"-","|")
                        print("|%3d | %-35s | %02d/%02d/%4d | %13d | %013d |  "%(i+1,a[i][0],a[i][1][0],a[i][1][1],a[i][1][2],a[i][2],a[i][3]))
                        print(" ",85*"-"," ")


            if ter == a[i][j]:
                print(" ",85*"-"," ")
                print("|",85*"-","|")
                print("|%25s %14s  |%9s |%10s %3s |%10s %4s| "%('Nome',"",' Data Nasc ','Rg',"",'CPF',""))
                print("|",85*"-","|")
                print("|%3d | %-35s | %02d/%02d/%4d | %13d | %013d |  "%(i+1,a[i][0],a[i][1][0],a[i][1][1],a[i][1][2],a[i][2],a[i][3]))
                print(" ",85*"-"," ")


while True:
    EnconTer()


def principal ():
    lista = geraLisCad(5)
    a = True
    while a == True:
        op = menu()
        if op == 1:
            while op == 1:
                opOrd = MenuImpLis()
                if opOrd == 1:
                    print("Mostrando Lista Ordenada Por Nome:\n\n")
                    ImpreLis(OrdLis(lista,0))
                elif opOrd == 2:
                    print("Mostrando Lista Ordenada Por Data de Nascimento:\n\n")
                    ImpreLis(OrdLis(lista,1))
                elif opOrd == 3:
                    print("Mostrando Lista Ordenada Por Rg:\n\n")
                    ImpreLis(OrdLis(lista,2))
                elif opOrd == 4:
                    print("Mostrando Lista Ordenada Por CPF:\n\n")
                    ImpreLis(OrdLis(lista,3))
                elif opOrd == 0:
                    break
                else:
                    print("\n\nValor Invalido:\n\n")
        elif op == 2:
            print("Digite o Termo para Procurar")
            termo = input()




#principal()












