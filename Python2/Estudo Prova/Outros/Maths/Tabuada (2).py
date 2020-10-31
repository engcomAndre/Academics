__author__ = 'ANDRE'
from os import  system
import os

def soma ():

    i = 0
    while (i <= 10):
        a = 0
        print("TABUADA DE ",end = " = ")
        print(i)
        print("")

        while a <=10 :
            print (i,end =" + ")
            print(a,end=" = ")
            print(i + a)
            a += 1
        i += 1
        print("")




def contador ():
    hor = 0
    min = 0
    seg = 0
    while True:
        while min <60:
            while seg < 60:
                print("%d : %d : %d" %(hor,min,seg))
                os.system("cls")
                seg+=1
            min +=1
            seg = 0
        hor +=1
        min = 0

contador()
