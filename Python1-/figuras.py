from turtle import *

def quadrado(tl):
    for i in range(4):
        forward(tl)
        right(90)

def arvore(tam,ger):
    if ger==0:
        return
    forward(tam)
    left(20)
    arvore(0.8*tam,ger-1)
    right(40)
    arvore(0.8*tam,ger-1)
    left(20)
    back(tam)
    

speed(0)
left(90)
penup()
back(200)
pendown()
arvore(80,10)
done()
