#coding:cp1252

def rec_fibonacci(num_termos,a = 0,b = 1):
    var = 0
    print(a,end = ",")
    if var+1 < num_termos:
        fibonacci(num_termos -1,a = b,b = a + b)


def whi_fibonacci(num_termos,a = 0,b = 1):
    while num_termos-1 > 0:
        print(a,end = ",")
        a,b = b,a + b
        num_termos-=1
    print(a)

def for_fibonacci(num_termos,a = 0,b = 1):
    for i in range(1,num_termos):
        print(a,end = " ,")
        a,b = b,a+b
    print(a)


for_fibonacci(5)
