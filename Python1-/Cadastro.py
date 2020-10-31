__author__ = 'AEC'
import  pickle
import random

def geralista():
    Nlis = []
    primeiro = ['ANDRÉ' , 'CRISTINA', 'ANGELO', 'DAVI','JOSÉ','ALICE','ADRIANO','MARIO','DEBORA','JONAS']
    segundo  = ['VIEIRA' , 'SILVA','SOUSA','COSTA','FERREIRA','ARAGÃO','MATOS','AGUIAR','MENDES','BARROS']
    terceiro = ['FARIAS','GUEDES','BEZERRA','LINHARES','BRANDÃO','LOPES','GENTIL','LIMA','DA LUZ','MEDEIROS']
    nome = random.choice (primeiro)
    a = random.randint(0,len(segundo)-1)
    nome += ' '+ segundo[a]
    b = random.randint(0,len(terceiro)-1)
    nome += ' '+ terceiro[b]
    Nlis.append (nome)
    return (Nlis)

def geraCad (pos):
    Cad = []
    Cad.append([pos])
    Cad.append(geralista())
    ano = random.randint(1900,2015)
    mes = random.randint(1,12)
    if mes == 4 or mes == 6:
        dia = random.randint(0,30)
    elif mes == 7 or mes == 11:
        dia = random.randint(0,30)
    elif mes == 2:
        dia = random.randint(1,28)
    elif mes == 2 and ano % 4 == 0:
        dia = random.randint(1,29)
    else:
        dia = random.randint(1,31)
    Cad.append([ano,mes,dia])

    print(Cad)

geraCad(1)

