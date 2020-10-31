import random
import pickle

def geraNome():
    nomes = ["Rodrigo","Priscila","Roberto","Aline","Pedro","Márcia","Marcelo","Vera","Joaquim","Fernando","Janaína","Bruno","Renata","Ramiro","Camila","Andréia","Milena","Patrícia","Ronaldo","Alberto"]
    sobres = ["Pereira","Moreira","Oliveira","Silva","Souza","Araújo","Bastos","Lopes","Maia","Nogueira","Lima","Rocha","Mota","Melo","Aquino","Lemos","Abreu","Cardoso","Correia","Santos"]
    nome = random.choice (nomes)
    ps = random.randint (0,len(sobres)-1)
    nome += " " + sobres[ps]
    ss = random.randint (0,len(sobres)-1)
    while ps == ss:
        ss = random.randint (0,len(sobres)-1)
    nome += " " + sobres[ss]
    return(nome)

def geraAluno(cod):
    alu = [cod]
    alu.append(geraNome())
    dia = random.randint (1,28)
    mes = random.randint (1,12)
    ano = random.randint (1980,2000)
    alu.append([ano, mes, dia])
    alu += [round(random.uniform(5,10),1),round(random.uniform (5,10),1)]
    return(alu)

def geraListaDeAlunos(na):
    la = []
    for i in range(na):
        la.append(geraAluno(i+1))
    return la

def mostreAluno(alu):
    print("{0:06d} {1:30s} {2:02d}/{3:02d}/{4:d}  ".format (alu[0],alu[1],
        alu[2][2],alu[2][1],alu[2][0]),end='')
    if alu[3] > 10.5:
        print("----",end='')
    else:
        print("{:4.1f}".format (alu[3]),end='')
    if alu[4] > 10.5:
        print("  ----",end='')
    else:
        print(" {:5.1f}".format (alu[4]),end='')
    if alu[3] > 10.5 or alu[4] > 10.5:
        print("  ----")
    else:
        print(" {:5.1f}".format (mediaParcial(alu)))

def mostreListaDeAlunos(la):
    print("\nLISTAGEM DE NOTAS")
    print(78*"-")
    print("Código Nome"+27*" "+"Nascimento   AF1   AF2    MP    AF    MF")
    print("------ ----"+26*"-"+" ----------  ----  ----  ----  ----  ----")
    for i in la:
        mostreAluno(i)

def menu():
    print("*************************")
    print("*   Controle de Notas   *")
    print("*************************\n")
    print("  1 - Lista de Notas")
    print("  2 - Cadastrar")
    print("  3 - Alterar dados")
    print("  0 - Fechar aplicativo")
    return input("\n  Escolha uma opção: ")

def mediaParcial(alu):
    return (2*alu[3]+3*alu[4])/5

def buscaAluno(cod,lis):
    for i in range(len(lis)):
        if cod == lis[i][0]:
            return i
    return -1

def cadastraAluno(cod):
    res = [cod]
    res.append(input("\n  Digite o nome do aluno: "))
    data = input("  Digita a data de nascimento (d/m/aaaa): ").split(sep = '/')
    data = [int(x) for x in data]
    data.reverse()
    res.append(data)
    res +=  [11,11]
    return res
    
def principal():
#    lis = geraListaDeAlunos(25)
    f = open("alunos.arq","rb")
    lis = pickle.load(f)
    f.close()
    ultCod = lis[0]
    lis = lis[1:]
    while True:
        op = menu()
        if op == "0":
            break
        if op == "1":
            print("\n    Lista de Notas")
            print("      1 - Ordenada pelo código do aluno")
            print("      2 - Ordenada pelo nome do aluno")
            print("      3 - Ordenada pelo data de nascimento do aluno")
            print("      4 - Ordenada pelo média do aluno")
            op2 = input("\n      Escolha uma opção: ")
            if op2 == "1":
                lis = sorted(lis, key = lambda alu: alu[0])
                mostreListaDeAlunos(lis)
            elif op2 == "2":
                lis = sorted(lis, key = lambda alu: alu[1])
                mostreListaDeAlunos(lis)
            elif op2 == "3":
                lis = sorted(lis, key = lambda alu: alu[2])
                mostreListaDeAlunos(lis)
            elif op2 == "4":
                lis = sorted(lis, key = lambda alu: mediaParcial(alu), reverse=True)
                mostreListaDeAlunos(lis)
            print("\n")
        elif op == "2":
            print("\nCadastrar aluno")
            alu = cadastraAluno(ultCod+1)
            lis.append(alu)
            ultCod += 1
        elif op == "3":
            print("\n  Alterar dados do aluno")
            op3 = int(input("\n  Digite o código: "))
            print("      1 - Alterar nome")
            print("      2 - ")
            print("      3 - Ordenada pelo data de nascimento do aluno")
            print("      4 - Ordenada pelo média do aluno")
            op2 = input("\n      Escolha uma opção: ")
            if op2 == "1":
                  ia = buscaAluno(op3,lis)
                  al = lis[ia]
                  no = input("Novo nome: ")
                  al[1] = no
                  lis[ia] = al
                  
            elif op2 == "2":
                lis = sorted(lis, key = lambda alu: alu[1])
                mostreListaDeAlunos(lis)
            elif op2 == "3":
                lis = sorted(lis, key = lambda alu: alu[2])
                mostreListaDeAlunos(lis)
            elif op2 == "4":
                lis = sorted(lis, key = lambda alu: mediaParcial(alu), reverse=True)
                mostreListaDeAlunos(lis)
            print("\n")
        else:
            print("\n  OPÇÃO INVÁLIDA\n")
    f = open("alunos.arq","wb")
    pickle.dump([ultCod]+lis,f)
    f.close()
    print("\n  Fim de Aplicativo\n")

principal()
    











