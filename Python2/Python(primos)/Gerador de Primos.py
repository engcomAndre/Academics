#-*-coding:UTF-8 -*-
import os
#gerador de primos
def geraprimo (termo):

    if termo % 2 == 0 and termo !=2:
        #print("O número %d não é primo,é divisivel por %d"%(termo,2))
        return False
    else:
        for i in range(3,(int((termo)/2)+1),2):
            if termo % i == 0:
                return F
                if i == termo:
                    return True
                else:
                    #print("O número %d não é primo,é divisivel por %d"%(termo,i))
                    #print("False")
                    return False


for numero in range(98459834597687687687876876876):
    if geraprimo(numero) == True:
        print("O número %d,     é primo"%(numero))






