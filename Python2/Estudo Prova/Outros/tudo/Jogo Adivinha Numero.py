# coding:utf8
import math
# Este programa calcula os três primeiros multiplos de um dado
# número, as raízes de uma equação de segundo grau com raízes 
# reais, área de circulo, triangulo e retangulo e o valor
# liquido de uma salario dado, dadas tmbm as aliquotas dos
# impostos sobre o valor bruto.

#x = float(input("Digite o valor desejado"))
#a = 1.0
#while a < 4:
 #  m = a*x
  # a = a+1.0
  # print m
 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = pow(b,2)- 4*(a*c)
if d < 0:
  print ("Raízes imaginárias")
else:
  x1 = (-b + math.sqrt(d))/(2*a)
  x2 = (-b - math.sqrt(d))/(2*a)
  print ("x1 é ", x1, "x2 é ",x2) 

#r = float(input("Digite o valor do raio"))
#pi = 3.1415
#area = pi*(r*r)
#b = float(input("Agora digite o valor da base do triangulo"))
#h = float(input("Idem altura do triangulo"))
#area_t = (b*h)/2
#print "a área do círculo é: ",area, "e a do triangulo é: ",area_t

