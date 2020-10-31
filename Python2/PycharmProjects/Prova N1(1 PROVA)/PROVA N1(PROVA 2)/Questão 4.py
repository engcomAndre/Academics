__author__ = 'ANDRE'
def fibonacci(numter):
    lis = [0,1]
    i = 0
    while numter > 0:
        lis.append(lis[i]+lis[i+1])
        numter -= 1
        i += 1
    print(lis)
fibonacci(7)
