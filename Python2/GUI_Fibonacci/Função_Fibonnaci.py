#-*-coding:cp1252-*-


def Fibo(par):
    a = 0
    b = 1
    for i in range(0,par-1):
        print(a,end = ",")
        a,b = b,a+b
    print(a)


Fibo(12)