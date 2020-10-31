import mysql.connector
from random import  randint

cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='bibliotecav0')
ponteiro = cnx.cursor()

lista = [' Travessa Evidências','Praça dos Enfartados','Rua do Corno','Travessa Maravilha Tristeza','Avenida Penetração Norte-Sul','Rua Só Nós Dois','Rua Borboletas Psicodélicas','Rua Grito de Alerta','Travessa Nave-Mãe','Rua Pato Donald']
listaAutor = ['Chico Buarque', 'José de Alencar', 'José Sarney', 'André de Leones', 'Paulo Coelho', 'Tony Bellotto',
              'Ana Beatriz Barbosa Silva', 'Lya Luft', 'Fernando Gabeira', 'Jô Soares']
lista_Editoras = ['Scholastic', 'Pearson', 'Reed Elsevier', 'ThomsonReuters', 'Wolters Kluwer', 'Hachette Livre',
                  'Grupo Planeta', 'McGraw-Hill Education', 'Random House', 'Holtzbrinck']
listaNome = ['Aricléia Café Chá',' Adolph Hitler Souza Lima',' Adolfo Hitler Modesto Costa',' Amim Amou Amado',' Anais Bezerra de Gusmão','América do Sul Brasil de Santana',' Araci do Precioso Sangue',' Antônio Veado Prematuro',' Antônio Dodói', 'Apurinã da Floresta Brasileira',' Agrícola Beterraba Areia',' Antônio Morrendo das Dores',' Antônio Rolão','Alma de Vera',' Amável Pinto']

def preenche_Biblioteca():
    ponteiro.execute("SELECT MAX(Cod_Biblioteca) FROM biblioteca ")
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        lista = ['A','B','C','D','E']
        for i in range(5):
            nome = 'Biblioteca '+ str(listaAutor[randint(0,len(lista)-1)])
            endereco  =  str(lista[randint(0,len(lista)-1)])
            requisicao = "INSERT INTO `biblioteca` (`Cod_Biblioteca`, `Nome`, `Endereco`, `Numero`) " \
                         "VALUES (NULL, '"+ nome +"', '"+ endereco +"', '"+ str(randint(10,100)) +"')"
            ponteiro.execute(requisicao)

def preenche_Titulos():
    ponteiro.execute("SELECT Cod_Biblioteca FROM biblioteca WHERE 1")
    temp_Cod_Biblioteca = ponteiro.fetchall()
    ponteiro.execute("SELECT Cod_Area_de_Conhecimento FROM area_de_conhecimento")
    temp_Cod_Area = ponteiro.fetchall()
    if not temp_Cod_Biblioteca[0][0] == None:
        ponteiro.execute("SELECT Cod_Editora FROM editoras WHERE 1")
        temp_Cod_Editoras = ponteiro.fetchall()
        for i in range(1,50,1):
            Cod_Biblioteca = temp_Cod_Biblioteca[randint(1,len(list(temp_Cod_Biblioteca)))-1][0]
            Cod_Editoras = temp_Cod_Editoras[randint(1,len(list(temp_Cod_Editoras)))-1][0]
            Cod_Area = temp_Cod_Area[randint(1,len(list(temp_Cod_Area)))-1][0]
            nome = 'Titulo '+str(i)
            requisicao = "INSERT INTO titulos (Cod_Titulo,Area_de_Conhecimento_Cod_Area_de_Conhecimento,Editoras_Cod_Editora,Biblioteca_Cod_Biblioteca,Nome)" \
                         "VALUES(NULL,'"+str(Cod_Area)+"','"+str(Cod_Editoras)+"','"+str(Cod_Biblioteca)+"','"+nome+"')"
            ponteiro.execute(requisicao)

def preenche_Autores():
    ponteiro.execute("SELECT MAX(Cod_Biblioteca) FROM biblioteca ")
    temp = ponteiro.fetchall()
    if not temp[0][0] == None:
        lista = ['A','B','C','D','E']
        for i in range(0,len(listaAutor)-1):
            endereco = str(lista[randint(0,len(lista)-1)])
            telefone = "("+str(randint(11,99))+") "+str(randint(986,999))+str(randint(000000,999999))
            requisicao = "INSERT INTO autores (Cod_Autores,Nome,Endereco,Numero,Telefone) " \
                         "VALUES (NULL,'"+listaAutor[i]+"','"+ endereco +"','"+ str(randint(10,1000))+"','"+telefone+"')"
            ponteiro.execute(requisicao)

def preenche_Editoras():
    ponteiro.execute("SELECT MAX(Cod_Editora) FROM editoras")
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        for i in range(0,len(lista_Editoras)-1):
            nome = lista_Editoras[i]
            endereco = str(lista[randint(0,len(lista)-1)])
            telefone = "("+str(randint(11,99))+") "+str(randint(986,999))+str(randint(000000,999999))
            requisicao = "INSERT INTO editoras (Cod_Editora,Nome,Endereco,Numero,Telefone) " \
                         "VALUES (NULL,'"+nome+"','"+endereco+"','"+str(randint(10,1000))+"','"+telefone+"')"
            ponteiro.execute(requisicao)

def preenche_Usuario():
    ponteiro.execute("SELECT MAX(Cod_Usuario) FROM usuario")
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        for i in range(0, 30):
            nome = listaNome[randint(0, len(lista) - 1)]
            endereco = str(lista[randint(0, len(lista) - 1)])
            telefone = "(" + str(randint(11, 99)) + ") " + str(randint(986, 999)) + str(randint(000000, 999999))
            requisicao = "INSERT INTO usuario (Cod_Usuario,Nome,Endereco,Numero,Telefone) " \
                         "VALUES (NULL,'" + nome + "','" + endereco + "','" + str(randint(10, 1000)) + "','" + telefone + "')"
            ponteiro.execute(requisicao)

def preenche_Aluno_Professor_Funcionario():
    ponteiro.execute("SELECT MAX(Cod_Aluno) FROM aluno")
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        ponteiro.execute("SELECT Cod_Usuario FROM usuario WHERE 1")
        temp = ponteiro.fetchall()
        i = 0
        while i < len(list(temp)):
            while temp[i][0] <= 10:
                requisicao = "INSERT INTO aluno (Cod_Aluno,Usuario_Cod_Usuario)" \
                             "VALUES (NULL,'" + str(temp[i][0]) + "')"
                i += 1
                ponteiro.execute(requisicao)

            while temp[i][0] <= 20:
                requisicao = "INSERT INTO professores (Cod_Professor,Usuario_Cod_Usuario)" \
                             "VALUES (NULL,'" + str(temp[i][0]) + "')"
                i += 1
                ponteiro.execute(requisicao)

            while i <= 29:
                requisicao = "INSERT INTO funcionario (Cod_Funcionario,Usuario_Cod_Usuario)" \
                             "VALUES (NULL,'" + str(temp[i][0]) + "')"
                i += 1
                ponteiro.execute(requisicao)

def preenche_Area_Conhecimento():
    ponteiro.execute("SELECT MAX(Cod_Area_de_Conhecimento) FROM area_de_conhecimento")
    temp = ponteiro.fetchall()
    if temp[0][0] == None:
        for i in range(20):
            descricao = 'Descricao '+ str(randint(100,999))
            requisicao = "INSERT INTO area_de_conhecimento (Cod_Area_de_Conhecimento,Descricao)" \
                     "VALUES (NULL,'"+descricao+"')"
            ponteiro.execute(requisicao)

def preenche_Autores_em_Titulos():
    ponteiro.execute("SELECT Cod_Autores FROM autores WHERE 1")
    temp_Autores = ponteiro.fetchall()
    ponteiro.execute("SELECT Cod_titulo FROM titulos WHERE 1")
    temp_Titulo = ponteiro.fetchall()
    if temp_Autores[0][0] != None and temp_Titulo[0][0] != None:
        for i in temp_Titulo:
            requisicao = "INSERT INTO autores_em_titulos (Autores_Cod_Autores,Titulos_Cod_titulo)" \
                         "VALUES('"+str(temp_Autores[randint(1,len(list(temp_Autores)))-1][0])+"','"+str(i[0])+"')"
            ponteiro.execute(requisicao)

def preenche_palavra_chave():
    ponteiro.execute("SELECT MAX(Cod_Palavra_Chave) FROM palavra_chave")
    temp = ponteiro.fetchall()
    print(temp[0][0])
    if temp[0][0] == None:
        for i in range(50):
            palavra = 'Palavra '+ str(i)
            requisicao = "INSERT INTO palavra_chave (Cod_Palavra_Chave,Descricao)" \
                         "VALUES (NULL,'"+ palavra +"')"
            ponteiro.execute(requisicao)

def preenche_palavra_chave_em_titulo():
    ponteiro.execute("SELECT Cod_Palavra_Chave FROM palavra_chave WHERE 1")
    temp_palavra_chave= ponteiro.fetchall()
    ponteiro.execute("SELECT Cod_titulo FROM titulos WHERE 1")
    temp_Titulo = ponteiro.fetchall()
    if temp_palavra_chave[0][0] != None and temp_Titulo[0][0] != None:
        for i in temp_Titulo:
            requisicao = "INSERT INTO palavra_chave_em_titulo (palavra_chave_Cod_Palavra_Chave	,titulos_Cod_Titulo)" \
                         "VALUES('" + str(temp_palavra_chave[randint(1, len(list(temp_palavra_chave))) - 1][0]) + "','" + str(
                i[0]) + "')"
            ponteiro.execute(requisicao)

def preenche_Exemplar():
    ponteiro.execute("SELECT Cod_Titulo FROM titulos WHERE 1")
    temp_Titulo = ponteiro.fetchall()
    if temp_Titulo[0][0] != None:
        for i in temp_Titulo:
            for k in range(0,randint(2,5)):
                requisicao = "INSERT INTO exemplares (Cod_Exemplar,titulos_Cod_Titulo) " \
                         "VALUES (NULL,'"+str(i[0])+"')"
                ponteiro.execute(requisicao)

def preenche_Emprestimo():
    ponteiro.execute("SELECT Cod_Exemplar FROM exemplares WHERE 1")
    temp_Exemplar = ponteiro.fetchall()
    ponteiro.execute("SELECT Cod_Usuario FROM usuario WHERE 1")
    temp_Usuario = ponteiro.fetchall()
    if temp_Exemplar[0][0] != None and temp_Usuario[0][0] != None:
        for i in range(0,randint(1,1000)):
            date = str(randint(1, 30)) + "/" + str(randint(1, 12)) + "/" + str(randint(199, 201)) + str(
                randint(0, 9))
            requisicao = "INSERT INTO emprestimo (Cod_Emprestimo,Exemplares_Cod_Exemplar,Usuario_Cod_Usuario,Data_Saida)" \
                         "VALUES(NULL,'"+str(temp_Exemplar[randint(1,len(list(temp_Exemplar)))-1][0])+"','"+str(temp_Usuario[randint(1,len(list(temp_Usuario)))-1][0])+"','"+date+"')"
            ponteiro.execute(requisicao)

def preenche_Banco_Biblioteca():
    preenche_Biblioteca()
    preenche_Editoras()
    preenche_Area_Conhecimento()
    preenche_Autores()
    preenche_Usuario()
    preenche_Titulos()

    preenche_Aluno_Professor_Funcionario()
    preenche_Autores_em_Titulos()
    preenche_Exemplar()
    preenche_Emprestimo()
    preenche_palavra_chave()
    preenche_palavra_chave_em_titulo()

def limpando_tabelas():
    ponteiro.execute("DELETE FROM aluno WHERE 1")
    ponteiro.execute("DELETE FROM professores WHERE 1")
    ponteiro.execute("DELETE FROM funcionario WHERE 1")
    ponteiro.execute("DELETE FROM usuario WHERE 1")
#Consultas
cnx.commit()
def consulta_1():
    requisicao = "SELECT titulos.Nome,autores.Nome " \
                 "FROM titulos,autores_em_titulos,autores " \
                 "WHERE titulos.Cod_Titulo = autores_em_titulos.titulos_Cod_Titulo " \
                 "AND autores_em_titulos.Autores_Cod_Autores = autores.Cod_Autores " \
                 "AND autores.Nome = 'José de Alencar'"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)

def consulta_2():
    requisicao = "SELECT exemplares.Cod_Exemplar,titulos.Nome " \
                 "FROM exemplares,titulos,area_de_conhecimento " \
                 "WHERE exemplares.titulos_Cod_Titulo = titulos.Cod_Titulo " \
                 "AND titulos.Area_de_Conhecimento_Cod_Area_de_Conhecimento = area_de_conhecimento.Cod_Area_de_Conhecimento " \
                 "AND area_de_conhecimento.Descricao = 'Descricao 131' " \
                 "ORDER by Cod_Exemplar " \
                 "ASC"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)

def consulta_3():
    requisicao = "SELECT autores.Nome " \
                 "FROM autores,autores_em_titulos,titulos,area_de_conhecimento " \
                 "WHERE autores.Cod_Autores = autores_em_titulos.Autores_Cod_Autores " \
                 "AND autores_em_titulos.titulos_Cod_Titulo = titulos.Cod_Titulo " \
                 "AND titulos.Area_de_Conhecimento_Cod_Area_de_Conhecimento = area_de_conhecimento.Cod_Area_de_Conhecimento " \
                 "AND area_de_conhecimento.Descricao = 'Descricao 297' " \
                 "ORDER BY autores.Nome " \
                 "ASC"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)

def consulta_4():
    requisicao = "SELECT titulos.Nome,usuario.Nome " \
                 "FROM titulos,exemplares,emprestimo,usuario " \
                 "WHERE titulos.Cod_Titulo = exemplares.titulos_Cod_Titulo " \
                 "AND exemplares.Cod_Exemplar = emprestimo.Exemplares_Cod_Exemplar " \
                 "AND emprestimo.Usuario_Cod_Usuario = usuario.Cod_Usuario AND usuario.Cod_Usuario = '1'" \
                 "ORDER BY usuario.Nome " \
                 "ASC"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)

def consulta_5():
    requisicao = "SELECT titulos.Nome,usuario.Nome " \
                 "FROM titulos,exemplares,emprestimo,usuario " \
                 "WHERE titulos.Cod_Titulo = exemplares.titulos_Cod_Titulo " \
                 "AND exemplares.Cod_Exemplar = emprestimo.Exemplares_Cod_Exemplar " \
                 "AND emprestimo.Usuario_Cod_Usuario = usuario.Cod_Usuario AND titulos.Nome = 'Titulo 3'"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)

def consulta_6():
    requisicao = "SELECT palavra_chave.Descricao,area_de_conhecimento.Descricao " \
                 "FROM area_de_conhecimento,titulos,palavra_chave_em_titulo,palavra_chave " \
                 "WHERE palavra_chave.Cod_Palavra_Chave = palavra_chave_em_titulo.titulos_Cod_Titulo " \
                 "AND palavra_chave_em_titulo.titulos_Cod_Titulo = titulos.Cod_Titulo " \
                 "AND titulos.Area_de_Conhecimento_Cod_Area_de_Conhecimento = area_de_conhecimento.Cod_Area_de_Conhecimento " \
                 "AND area_de_conhecimento.Descricao = 'Descricao 782' " \
                 "ORDER BY palavra_chave.Descricao " \
                 "ASC"
    ponteiro.execute(requisicao)
    temp = ponteiro.fetchall()
    for i in temp:
        print(i)
