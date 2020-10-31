__author__ = 'ANDRE'
import random
#adivinha o numero
def adivinha ():

    a = 1
    contp = 0
    contc = 0
    while a == 1:
        print("Adivinhe o numero")
        res = random.randint(1,100)
        palpite = 0
        computer = 0
        ten = 1
        b = 1
        c = 100
        print(ten,end = "")
        print(" Tentativa,Digite seu palpite:")

        while (palpite != res and computer != res):
            palpite = int(input())
            computer = random.randint(1,100)
            print("Computador : ",end="")
            print(computer)
            print("")
            ten += 1
            print(ten,end="")

            print(" Tentativas,Digite seu palpite:")


            if (palpite > res and computer > res):
                print("VOCE ERROU PRA MAIS")
                print("COMPUTADOR ERROU PRA MAIS")

                if palpite > computer:
                    c = computer
                else:
                    c = palpite


            elif (palpite  < res and computer < res):
                print("VOCE ERROU PRA MENOS")
                print("COMPUTADOR ERROU PRA MENOS")
                if palpite > computer:
                    b = palpite
                else:
                    b = computer

            elif (palpite > res and computer < res):
                print("VOCE ERROU PRA MAIS")
                print("COMPUTADOR ERROU PRA MENOS")
                c = palpite
                b = computer

            else:
                print("VOCE ERROU PRA MENOS")
                print("COMPUTADOR ERROU PRA MAIS")

                b = palpite
                c = computer

            computer = random.randint(b,c)

        if palpite == res and computer == res :
            print("Ambos Acertaram")
            contc+= 1
            contp +=1


        elif (palpite == res):
            print("Voce acertou em ",end="")
            print(ten,end="")
            print(" Tentativas")
            contp += 1

        else:
            print("Computador acertou em ",end="")
            print(ten,end="")
            print(" Tentativas")
            contc += 1
        print("")
        print("Escore")
        print("Jogador = ",end ="")
        print(contp)
        print("Computador = ",end ="")
        print(contc)
        print("")


adivinha()




