def soma (a,b):                                                                         
    return(a+b)
        
def multiplica (a,b):
    b = soma (a,5)
    print (a*(soma(a,5)))
    
    
#PROCEDIMENTO CALCULA OS TERMOS DE UMA PROGRESSÃO ARITMÉTICA
#COM USO DO COMANDO FOR
def PA (PrimeiroTermo,NumerodeTermos,razão):
    for i in range (1,NumerodeTermos,1):
        print (PrimeiroTermo,"-",end=" ")
        PrimeiroTermo += razão
    print (PrimeiroTermo)


def whiPA (PrimeiroTermo,NumerodeTermos,razão):
    while NumerodeTermos > 1:
        print (PrimeiroTermo,"-",end=" ")
        PrimeiroTermo += razão
        NumerodeTermos -=1
    print (PrimeiroTermo)

def recPA (PrimeiroTermo,NumerodeTermos,razão):
    if NumerodeTermos > 1:
        print (PrimeiroTermo,"-",end=" ")
        PrimeiroTermo = PrimeiroTermo + razão
        recPA(PrimeiroTermo,NumerodeTermos - 1,razão)
    elif NumerodeTermos == 1:
        recPA(PrimeiroTermo,NumerodeTermos - 1,razão)
        print(PrimeiroTermo,".", end="")
    
        
recPA (1,10,1)

    

