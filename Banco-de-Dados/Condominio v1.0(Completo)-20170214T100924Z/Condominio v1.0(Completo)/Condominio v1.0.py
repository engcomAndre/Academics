import mysql.connector
from random import randint

cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='condominio')
ponteiro = cnx.cursor()


#Inserindo Lote de dados tabela cadastrogeraldepessoas
def InserirLote(maxElem):
    requisicao = "SELECT MAX(CodPessoa) FROM cadastrogeraldepessoas"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        for i in range (1,maxElem+1,1):
            nome = 'Pessoa ' + str(i)
            end = 'Endereço ' + str(i)
            requisicao = "INSERT INTO cadastrogeraldepessoas (CodPessoa,Nome,Endereco) " \
                         "VALUES('0','"+ nome +"','"+ end +"')"
            ponteiro.execute(requisicao)
            cnx.commit()

        #Inserindo Lote de dados tabela condominio
        for i in range (1,6,1):
            nome = 'Condominio ' + str(i)
            end = 'Endereço ' + str(i)
            requisicao = "INSERT INTO condominio (CodCondominio,Nome,Endereco) " \
                         "VALUES('0','"+ nome +"','"+ end +"')"
            ponteiro.execute(requisicao)
            cnx.commit()

        #Inserindo Lote de dados tabela condominos
        requisicao = "SELECT CodPessoa FROM cadastrogeraldepessoas " \
                     "WHERE cadastrogeraldepessoas.CodPessoa < 10 "
        ponteiro.execute(requisicao)
        temp = ponteiro.fetchall()
        for i in temp:
            requisicao = "INSERT INTO condomino (Cod_Condomino,CadastroGeraldePessoas_CodPessoa) " \
                         "VALUES('0','"+ str(i[0]) +"')"
            ponteiro.execute(requisicao)
            cnx.commit()

        # Inserindo Lote de dados tabela inquilinos
        requisicao = "SELECT CodPessoa FROM cadastrogeraldepessoas WHERE cadastrogeraldepessoas.CodPessoa >= 10 "
        ponteiro.execute(requisicao)
        temp = ponteiro.fetchall()
        for i in temp:
            requisicao = "INSERT INTO inquilino (CodInquilino,CadastroGeraldePessoas_CodPessoa) " \
                         "VALUES('0','" + str(i[0]) + "')"
            ponteiro.execute(requisicao)
            cnx.commit()

        # Inserindo Lote de dados tabela unidadeshabitacionais
        requisicao = "SELECT CodCondominio FROM condominio WHERE 1"
        ponteiro.execute(requisicao)
        temp = ponteiro.fetchall()
        for i in temp:
            for j in range(10):
                cod_cond = randint(1,9)
                area = randint(i[0]*j, 500)
                end = 'Condominio: ' + str(i[0])+' N°:'+str(j)
                requisicao = "INSERT INTO unidadeshabitacionais (CodUH,Condomino_Cod_Condomino,Condominio_CodCondominio,Area,Endereço)" \
                             " VALUES('0','" + str(cod_cond) + "','" + str(i[0]) + "','"+str(area)+"','"+end+"')"
                ponteiro.execute(requisicao)
                cnx.commit()

        # Inserindo Lote de dados tabela sindico
        requisicao = "SELECT CodCondominio FROM condominio WHERE 1"
        ponteiro.execute(requisicao)
        temp = ponteiro.fetchall()
        for i in range(1, 6):
            date = str(randint(1, 30)) + "/" + str(randint(1, 12)) + "/" + str(randint(199, 201)) + str(
                randint(0, 9))
            requisicao = "INSERT INTO  sindico (cod_Sindico,Condominio_CodCondominio,Condomino_Cod_Condomino,Vigencia) " \
                         "VALUES('0','" + str(i) + "','" + str(6 - i) + "','" + str(date) + "')"
            ponteiro.execute(requisicao)
            cnx.commit()

        # Inserindo Lote de dados tabela Cod_Contrato
        requisicao = "SELECT CodUH FROM unidadeshabitacionais WHERE 1"
        ponteiro.execute(requisicao)
        temp = ponteiro.fetchall()
        for i in range(1, 12):
            j = randint(1, 50)
            requisicao = "INSERT INTO  contrato_loc (Cod_Contrato,UnidadesHabitacionais_CodUH,Inquilino_CodInquilino) " \
                         "VALUES('0','" + str(j) + "','" + str(i) + "')"
            ponteiro.execute(requisicao)
            cnx.commit()


InserirLote(20)
def consulta1():
    n = 2
    requisicao = "SELECT CodUH,Condomino_Cod_Condomino FROM unidadeshabitacionais WHERE Condominio_CodCondominio = '"+str(n)+"'"
    ponteiro.execute(requisicao)
    for i in ponteiro:
        print("Código da Unidade = "+str(i[0])+"  Condomino = "+str(i[1]))
def consulta2():
    n = 100
    requisicao = "SELECT condominio.Nome FROM condominio,unidadeshabitacionais WHERE condominio.CodCondominio = unidadeshabitacionais.Condominio_CodCondominio AND unidadeshabitacionais.Area > '"+str(n)+"'"
    ponteiro.execute(requisicao)
    for i in ponteiro:
        print(i[0])
def consulta3():
    n = 160
    requisicao = "SELECT cadastrogeraldepessoas.Nome " \
                 "FROM sindico,condomino,cadastrogeraldepessoas,unidadeshabitacionais " \
                 "WHERE sindico.Condomino_Cod_Condomino = condomino.Cod_Condomino " \
                 "AND condomino.CadastroGeraldePessoas_CodPessoa = cadastrogeraldepessoas.CodPessoa " \
                 "AND unidadeshabitacionais.Condomino_Cod_Condomino = condomino.Cod_Condomino " \
                 "AND unidadeshabitacionais.Area > '"+str(n)+"'"
    ponteiro.execute(requisicao)
    for i in ponteiro:
        print(i)
def consulta4():
    n = 160
    requisicao = "SELECT condomino.Cod_Condomino FROM condomino,unidadeshabitacionais " \
                 "WHERE condomino.Cod_Condomino = unidadeshabitacionais.Condomino_Cod_Condomino " \
                 "AND unidadeshabitacionais.Area > '"+str(n)+"'"
    ponteiro.execute(requisicao)
    for i in ponteiro:
        print("Condomino = "+str(i[0]))

consulta3()




