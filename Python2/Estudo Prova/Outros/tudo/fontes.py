

#coding:utf8
#qpy:console
#
# Jogo de acerte o número
#
import random
random.seed()
valor = random.randint(1,99)
chute = 0
tentativas = 0
#os.system("clear") # No linux ou mac os
os.system("cls") # No windows, wince, nt
while chute != valor:
    chute = int(input("Digite o seu palpite "))
    tentativas = tentativas + 1
    if chute == valor:
        print ("Parabéns, você acertou em ",tentativas," tentativas!!!!")
    elif chute < valor:
        print ("Errou para menos na tentativa ",tentativas)
    else:
        print ("Errou para mais na tentativa ",tentativas)
# fim do programa







#coding:utf8
#qpy:console
#
#
os.system("cls") # No windows, wince, nt
vetor = []
n = int(raw_input("Digite a quantidade de elementos a ser adicionada -> "))
i = 0
while i<n:
    temp = input("Digite o elemento a ser adicionado ->")
    vetor.append(temp)
    i=i+1
print ("Vetor = ",vetor)
# fim do programa












Programa 19 – Receber elementos selecionar o maior e o menor.
#coding:utf8
#qpy:console
#
#
import os # Biblioteca de funcoes do sistema operacional
os.system("clear") # No linux ou mac os
# os.system("cls") # No windows, wince, nt
#
#
vetor = []  # Declara o vetor
# Solicita o número de elementos
n = int(raw_input("Digite a quantidade de elementos a ser adicionada -> "))
# Declara o i
i = 0
# Recebe os elementos do vetor (Números inteiros)
while i<n:
    temp = int(raw_input("Digite o elemento a ser adicionado ->"))
    vetor.append(temp)
    i=i+1
# Declara as variáveis menor e maior
menor = vetor[0]
maior = vetor[0]
 
# Reinicia o i
i = 0
 
#Laço de seleção do menor e do maior
while i<len(vetor):
    if vetor[i]< menor:
        menor = vetor[i]
    if vetor[i]> maior:
        maior = vetor[i]
    i = i + 1
 
#Imprime o resultado
print "Vetor dado  : ",vetor
print "Menor valor : ",menor
print "Maior valor : ",maior
# fim do programa











Programa 22 – Pesquisa Linear
	
#coding:utf8
#qpy:console
#
#
import os # Biblioteca de funcoes do sistema operacional
os.system("clear") # No linux ou mac os
# os.system("cls") # No windows, wince, nt
#
#
vetor = []  # Declara o vetor
# Solicita o número de elementos
n = int(raw_input("Digite a quantidade de elementos a ser adicionada -> "))
# Declara o i
i = 0
# Recebe os elementos do vetor (Números inteiros)
while i<n:
    temp = int(raw_input("Digite o elemento a ser adicionado ->"))
    vetor.append(temp)
    i=i+1
elemento_procurado = int(raw_input("Digite o elemento a localizar->"))
i=0
posicao = -1
while i<len(vetor):
    if elemento_procurado == vetor[i]:
        posicao = i
    i = i + 1
print "Vetor Recebido     : ",vetor
print "Elemento procurado : ",elemento_procurado
if posicao == -1:
    print "Elemento não encontrado"
else:
    print "Elemento encontrado na posição ",posicao
 
# fim do programa











Programa 25 – Intercalação de Vetores
	
#coding:utf8
#qpy:console
#
#
import os # Biblioteca de funcoes do sistema operacional
os.system("clear") # No linux ou mac os
# os.system("cls") # No windows, wince, nt
#
#
vetor = []  # Declara o vetor1
vetor2 = [] # Declara o vetor2
 
# Solicita o número de elementos para o vetor 1
n = int(raw_input("Digite a quantidade de elementos a ser adicionada -> "))
# Declara o i
i = 0
# Recebe os elementos do vetor 1 (Números inteiros)
while i<n:
    temp = int(raw_input("Digite o elemento a ser adicionado ->"))
    vetor.append(temp)
    i=i+1
i=0
# Recebe os elementos do vetor 2
n2 = int(raw_input("Quantos elementos no vetor 2 -->"))
while i<n2:
    temp = int(raw_input("Digite o elemento a ser adicionado ->"))
    vetor2.append(temp)
    i=i+1
 
# Três variaveis que serao os indices de referência
i = 0
j = 0
k = 0
vetor3 = []
while i< len(vetor)+len(vetor2):
    if j<len(vetor):
        vetor3.append(vetor[j])
        i = i + 1
        j = j + 1
    if k<len(vetor2):
        vetor3.append(vetor2[k])
        i = i + 1
        k = k + 1
 
print "Vetor 1 Recebido  : ",vetor
print "Vetor 2 Recebido  : ",vetor2
print "Vetor Intercalado : ",vetor3
 
# fim do programa










Programa 27 – Tabuada

#coding:utf8
#qpy:console
#
# programa para gerar a tabuada de multiplicar
#
#
import os # Biblioteca de funcoes do sistema operacional
os.system("clear") # No linux ou mac os
# os.system("cls") # No windows, wince, nt
i = 1
print "Tabuada de Multiplicar "
while i < 10:
    j = 1
    print "--------------"
    while j < 10:
        print i," * ",j," = ",i*j
        j = j + 1
    i = i + 1
 
# fim do programa











programa 28 – Relógio Digital (Não funciona no IDLE. Somente nos terminais de comando)
#coding:utf8
#qpy:console
#
# programa para gerar a tabuada de multiplicar
#
#
import time
import os # Biblioteca de funcoes do sistema operacional
os.system("clear") # No linux ou mac os
# os.system("cls") # No windows, wince, nt
i = 0
while i < 24:
    j = 0
    while j < 60:
        k = 0
        while k < 60:
            os.system("clear")
            print i,":",j,":",k
            k = k + 1
            #time.sleep(1)
        j = j + 1
    i = i + 1
 
# fim do programa









Programa 29 – Primos
	
#coding:utf8
#qpy:console
#
# quais primos existem até n
#
import os
os.system("clear")
#
q = int(raw_input("Digite um número limite "))
for n in range(2,q):
    for x in range(2,n):
        if n % x == 0:
            print n,"igual a ", x," * ", n/x
            break
    else:
        # programa chegou aqui por não ter executado  o break
        print n," é um número primo "









Programa 30 – Fatorial não recursiva
	
#encoding:utf8
#qpy:console
#
#
import os
os.system("clear")
#
# definindo a função fatorial
def fat(n):
    if n < 0:
        return "Erro, não existe fatorial de número negativo "
    elif n == 0:
        return 1
    else:
        fat = n
        for i in range(1,n):   
            fat = fat * i
        return fat
# fim da função
#
x = int(raw_input("Digite o valor para calcular o fatorial ->"))
#
# Chamada à função
 
print "O fatorial de ", x, " é ",fat(x)
 
# fim do programa












Programa 31 – Fatorial recursiva

#encoding:utf8
#qpy:console
#
# implementa a funcao fatorial recursivamente
#
import os
os.system("clear")
 
def fat(n):
    if n< 0:
        return "Erro ...."
    elif n == 0:
        return 1
    else:
        return n * fat(n-1)
# fim da função
#
#
x = int(raw_input("Digite o valor a ser calculado o fatorial "))
print "Fatorial de ",x, " é ",fat(x)
 
# fim do programa

















programa 32 – Série de fibonacci recursiva
#encoding:utf8
#qpy:console
import os
os.system("clear")
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
 
x = int(input("Digite o tamanho da série "))
print "Série gerada : ",
for n in range(1,x+1):
    print fib(n),







Programa 33 – Pesquisa binária

#encoding:utf8
#qpy:console
#
# Exemplo de pesquisa binária
#
import os
os.system("clear")
#
#
def localiza(lista,valor):
    def pesquisa_binaria(min,max):
        if min==max:
            return min
        else:
            meio=(max+min)/2
            if valor>lista[meio]:
                return pesquisa_binaria(meio+1,max)
            else:
                return pesquisa_binaria(min,meio)
    # fim da função interna pesquisa_binaria
    i = pesquisa_binaria(0,len(lista)-1)
    if lista[i]==valor:
        print valor,"encontrado na posicao",i
    else:
        print valor,"nao encontrado"
# fim da função localiza
l = input("Digite a lista a ser pesquisada \
    \nLembre que deve estar em ordem crescente -> ")
v = input("Qual o valor a pesquisar ")
 
localiza(l,v)
 
# fim do programa







Desafio recursivo. Imprima uma pequena lista de números dados o valor inicial e final sem usar laços (for e while) e sem usar o range()
def desafio(num,fim):
    print num,
    if num!=fim:
        desafio(num+1,fim)
desafio(input("Digite o numero inicial: "),input("Digite o numero final: "))







#verificar se uma lista é permutação da outra

def verificaLis(lis1,lis2):
    cont=0
    for i in range(len(lis2)):
        if lis1[i] in lis2:
            cont+=1
    if cont==len(lis2):
        print 'lis1 eh permutacao de lis2'
    else:
        print 'lis1 nao eh permutacao de lis2'
#FIM










#Dada uma lista de tamanho qualquer. Por exemplo [3,1,5,67,8]. Calcular todas as permutações possíveis de a. Dica: Use recursividade.

def permutacoes(lista):
if len(lista) == 1:
return [lista]
p = lista[0]
r = lista[1:]
res = []
for a in permutacoes(r):
for i in range(len(p)+1):
res += [a[:i]+[p]+ a[i:]]
return res








#Introduzindo POO.
#Programa 43
	
#encoding:utf8
#qpy:console
#
# iniciando a orientação a objetos em python
#
import math
import os
os.system("clear")
 
class Triangulo:
    c1 = 0
    c2 = 0
    def h(t): # a funcao deve ter pelo menos um argumento
        return math.sqrt(t.c1**2 +t.c2**2)
# fim da classe
t = Triangulo()
t.c1 = input("Digite o tamanho do cateto 1 ")
t.c2 = input("Digite o tamanho do cateto 2 ")
print "hipotenusa é ",t.h()










#CRUD COMPLETO

#encoding:utf8
#qpy:console
#
import math
import os
class Aluno:
    def __init__(self, nome = 'None', endereco = 'None', email = 'None'):
        self.nome = nome
        self.endereco = endereco
        self.email = email
    def update(self):
        self.nome = input("Digite o nome do aluno ")
        self.endereco = input("Digite o endereco do aluno ")
        self.email = input("Digite o e-mail do aluno ")
    def __str__(self):
        return("-----------\nAluno: "+self.nome+"\nEnd: "+self.endereco+"\ne-mail:"+self.email)
 
# fim da classe
# inicio do programa
lista = []
 
lista.append(Aluno("Test","ponte ghi","e@f.com"))
 
while True:
     print("===========================================")
     print("Escolha uma opção abaixo:")
     print("<1> Cadastrar um Aluno")
     print("<2> Listar os Alunos")
     print("<4> Pesquisar por nome")
     print("<5> Apagar por nome")
     print("<6> Atualizar cadastro por nome")
     print("<0> Sair do Programa")
     escolha = input("Digite sua escolha e pressione <enter> ")
     if (escolha == "1"):
          obj = Aluno()
          obj.update()
          lista.append(obj)
     elif (escolha == "2"):
          for i in lista:
                print(i)
     elif (escolha == "4"):
          nomePesq = input("Digite o nome a pesquisar")
          for i in lista:
                if (i.nome == nomePesq):
                     print(i)
     elif (escolha == "5"):
          nomePesq = input("Digite o nome a ser apagado")
          for i in lista:
                if (i.nome == nomePesq):
                     lista.remove(i)
     elif (escolha == "6"):
          nomePesq = input("Digite o nome do registro a ser atualizado")
          for i in lista:
                print(i)
                if (i.nome == nomePesq):
                     i.update()
     elif (escolha == "0"):
          break
 
print("Fim")










#SOLUCOES PROVA

#QUESTAO 1

def maior(lista):
    maior = lista[0]
    for i in lista:
        if maior < i:
            maior = i
    return maior
     
a,b=input("digite as listas separadas por virgula ")
c=[]
for k in range(len(a)+len(b)):
    if len(a) > 0 and len(b) >0:
        ma = maior(a)
        mb = maior(b)
        if ma>mb:
            c.append(ma)
            a.remove(ma)
        else:
            c.append(mb)
            b.remove(mb)
    elif  len(a)==0:
            mb = maior(b)
            c.append(mb)
            b.remove(mb)
    elif  len(b)==0:
            ma = maior(a)
            c.append(ma)
            a.remove(ma)
 
print c


Atenção.
1. Há outras soluções. Soluções muito parecidas costumam ser cópia/pesca/etc
2. Vc pode usar o operador max do python no lugar da função maior definida acima. Diminui 6 linhas.






#Questão 2.
#encoding:utf8
#
import os
 
class Registro:
    def __init__(self, dado=""):
        self.proximo = ""
        self.anterior = ""
        self.dado = dado
 
primeiro = Registro()
atual = primeiro
ultimo = primeiro
 
# inicio do programa
while True:
    os.system("clear")
    print "Escolha uma opção abaixo:"
    print "<1> Cadastrar um registro"
    print "<2> Listar os registros "
    print "<3> Pesquisar por nome "
    print "<4> Sair do Programa"
    escolha = raw_input("Digite sua escolha e pressione <enter> ")
    if escolha == "1":
        os.system("clear")
        dado = raw_input("Digite o dado a ser cadastrado")
        obj = Registro(dado)
        if primeiro.dado == "":
            primeiro = obj
            ultimo = primeiro
        else:
            ultimo.proximo = obj
            obj.anterior = ultimo
            ultimo = ultimo.proximo
    elif escolha == "2":
        atual = primeiro
        while True:
            print atual.dado
            if atual.proximo == "":
                break
            else:
                atual = atual.proximo
        raw_input("Tecle enter para continuar ")
    elif escolha == "3":
        atualdesc = primeiro
        atualasc = ultimo
        texto = raw_input("Digite o texto a ser pesquisado ")
        desc=True
        while atualdesc != atualasc:
            if atualdesc.dado == texto:
                print "Encontrado ",atualdesc.dado
                break;
            if atualasc.dado == texto:
                print "Encontrado ",atualasc.dado
                break;
            if desc:
                atualdesc = atualdesc.proximo
            else:
                atualasc = atualasc.anterior
            desc = not desc
        else:
            print("Não encontrado. ")
        raw_input("Tecle enter para continuar")
    elif escolha == "4":
        break

OBS: O else associado ao while é opcional (linha 61) (Isto só existe em python)












#Questão 3
	
def intercalar(a,b):
    i = 0
    j = 0
    c = []
    while len(c) < len(a) + len(b):
        while i<len(a) and j <len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        if i<len(a):
            c.append(a[i])
            i+=1
        if j<len(b):
            c.append(b[j])
            j+=1
    return c
 
def merge(a):
    if len(a) == 1:
        return a
    metade = len(a)/2
    b = a[0:metade]
    c = a[metade:]
    bord = merge(b)
    cord = merge(c)
    resultado = intercalar(bord,cord)
    return resultado
 
 
lista = input("Entre com a lista ")
saida = merge(lista)
print "Lista original ",lista
print "Ordenada ",saida









#Use a sobrecarga de operadores para criar uma classe vetor que faz a soma de vetores.
#Ex. Seja o vetor a = [1,2,3] e o vetor b = [4,5,6]. A soma será ##[5,7,9]. Obs: O vetor pode ter qualquer tamanho e não se pode usar o #numpy,scipy,etc
 

class Vetor():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        novo = Vetor()
        novo.x = self.x + other.x
        novo.y = self.y + other.y
        novo.z = self.z + other.z
        return(novo)
    def __str__(self):
        return(str(self.x) + ', ' + str(self.y) + ', ' + str(self.z))
 
t1 = Vetor(1, 2, 3)
t2 = Vetor(5, 6, 7)
 
print(t1 + t2)




#atributos dinamicos 

#encoding:utf8
#qpy:console
#
#  Executa as funções dinamicamente de acordo com o número fornecido pelo usuário
#
class  DepositoAtributos:
    def calcula1(self):
        print "Eu sou  a função calcula 1"
    def calcula2(self):
        print "Eu sou a função calcula 2"
    def calcula3(self):
        print "Eu sou a função calcula 3"
numero = input("Digite o numero da função que vc deseja executar (Número de 1 a 3)")
f = getattr(DepositoAtributos(),'calcula'+str(numero))()
#Para executar vc digita 1,2 ou 3 ao ser solicitado e ele executa a função de acordo com o número dado.










#Esta função também pode ser usada para capturar atributos normais. Ex.
	
#encoding:utf8
#qpy:console
#
#  Executa as funções dinamicamente de acordo com o número fornecido pelo usuário
#
class  DepositoAtributos:
    x=1000
    y=234
    z=432
at = raw_input("Digite o atributo que voce quer ver x,y ou z")
print getattr(DepositoAtributos(),at)












#lista encadeada em python

#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Objetivo :  Implementar uma lista encadeada simples
#   Entrada : Um valor qualquer
#   Saida: ...
#   Autor: jonathan
class ListaEncadeada:
   # Declaracao dos atributos desta Classe
   valorOrbital = None
   proximo = None
   # Fim declaracao


   # Nesta secao encontram-se os metodos para acesso
   # dos respectivos atributos
   def getValorOrbital(self):
      return(self.valorOrbital)
   def getProximo(self):
      return(self.proximo)
   def setValorOrbital(self, valorOrbital):
      self.valorOrbital = valorOrbital
   def setProximo(self, proximo):
      self.proximo = proximo
   # Fim declaracao Metodos Get e Set   


   # Metodo para Insercao 
   def insereInicio(self, raiz, valorOrbital):
      temporario = ListaEncadeada()
      # o atributo proximo aponta para o atributo
      # proximo da raiz   
      temporario.setProximo(raiz.getProximo())
      temporario.setValorOrbital(valorOrbital)
      # o atributo proximo da raiz, aponta para temporario
      raiz.setProximo(temporario)
   # Fim insercao


   # Metodo para percorrer lista
   def percorreListaEncadeada(self, raiz):
      temporario = ListaEncadeada()   
      temporario = raiz.getProximo()
      while(temporario != None):
         print temporario.getValorOrbital()
         # incremento do temporario
         temporario = temporario.getProximo()
   # Fim percorrimento


   # Metodo para remocao
   def removeInicio(self, raiz):
      temporario = ListaEncadeada()
      temporario = raiz.getProximo()
      print temporario.getValorOrbital()
      raiz.setProximo(temporario.getProximo())
      temporario = None
   # Fim remocao












#LISTA LIGADA POO Uma coisa legal acerca da classe ListaLigada é que ela provê um lugar natural para se colocar funções envoltórias como imprimeDeTrasParaFrenteLegal, que podemos transformar em um método da classe ListaLigada:

class ListaLigada:
  def __init__(self):
    self.comprimento = 0
    self.cabeca = None


class ListaLigada:
  ...
  def imprimeDeTrasParaFrente(self):
    print "[",
    if self.cabeca != None :
      self.cabeca.imprimeDeTrasParaFrente()
    print "]",


class No:
  ...
  def imprimeDeTrasParaFrente(self):
    if self.proximo != None:
      rabo = self.proximo
      rabo.imprimeDeTrasParaFrente()
    print self.carga,

#FIM!!!


