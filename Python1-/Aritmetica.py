# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 08:12:29 2015

@author: Guedes
"""

def progArit(nt,ti,ra,nc=2):
    """
    Procedimento que mostra os termos de uma Progressão Aritmética
    Parâmetros:
      nt - Número de termos
      ti - Termo inicial
      ra - Razão
      nc - Número de casas decimais dos termos (opcional)
    """
    while nt>1:
        print(round(ti,nc),end=", ")
        ti = ti+ra
        nt = nt-1
    print(round(ti,nc))

def mdc(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def mdcR(a,b):
    if a == b:
        return a
    elif a > b:
        return mdcR(a-b,b)
    else:
        return mdcR(a,b-a)

def mdcR2(a,b):
    if b == 0:
        return a
    else:
        return mdcR2(b,a%b)

def mdc2(a,b):
    while b != 0:
        a, b = b, a%b
    return a
    
def mmc(a,b):
    pa, pb = a, b
    while a != b:
        if(a > b):
            b += pb
        else:
            a += pa
    return a

def mmc2(a,b):
    pa = a
    pb = b
    return mmcR(a,b,pa,pb)
            
def mmcR(a,b,x,y):
    if a==b: return a
    if a > b: return mmcR(a,b+y,x,y)
    return mmcR(a+x,b,x,y)

print(mmc2(15,12))























