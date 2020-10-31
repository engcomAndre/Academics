import pickle,os

def gerando():
    f = open("TESTE1.txt","w")

    f.close()

def abrindo():
    f = open("TESTE1.txt","w")
    a = "AQUI VAI QUALQUER COISA"
    f.write(a)
    f.close()
abrindo()



#gerador de primos
def geraprimo (termo):
    for i in range(2,termo+1):
        if termo % i == 0:
            if i == termo:
                #print("True")
                return True
            else:
                #print("False")
                return False

def primo():
    num = 1
    while True:
        if geraprimo(num) == True:
            print (num)
        num+=2

primo()



