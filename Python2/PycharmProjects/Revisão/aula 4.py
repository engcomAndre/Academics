__author__ = 'ANDRE'


def complis():
    lisa = [1,2,3]
    lisb = [3,2]
    a = 0

    while a < len(lisa):
        if lisa [a] in lisb:
            a +=1

        else:
            print("nao contida")
            return 0
    print("contida")


def complisF():
    lisa = [9,2,3,4,1]
    lisb = [1,3,2,4]

    for a in range (0,len(lisa)):
        if lisa[a] in lisb :
            pass

        else:
            print("nao contida")
            return 0
    print("Esta contida")


complisF()