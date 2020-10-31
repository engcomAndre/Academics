__author__ = 'ANDRE'

import os

#fibo
# 0 , 1 , 1 , 2 , 3 , 5 ,8 , 13 , 21
def fibonacci(numter):
    lis = [0,1]
    a = 1
    b = 0
    c = 1
    while numter > 2:
        a = lis[b] + lis[c]
        b +=1
        c +=1
        lis.append(a)
        numter -=1
        os.system("cls")
    print(lis)

fibonacci(10)
