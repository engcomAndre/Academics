__author__ = 'ANDRE'
#criar classe para calcular diferenca entre duas areas

import math
class coroa:
    def __init__(self,tamraio):
        self.raio = tamraio

def calcarea():
    cmaior = coroa(10)
    cmenor = coroa(5)
    return (0.5*math.pi*math.pow(cmaior.raio,2))-(0.5*math.pi*math.pow(cmenor.raio,2))
print(calcarea())








