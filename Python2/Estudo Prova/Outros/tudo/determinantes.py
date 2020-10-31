print "Entre com os valores:"


a00 = float(raw_input('Digite o valor de a00 '))
a01 = float(raw_input('Digite o valor de a01 '))
a02 = float(raw_input('Digite o valor de a02 '))
a10 = float(raw_input('Digite o valor de a10 '))
a11 = float(raw_input('Digite o valor de a11 '))
a12 = float(raw_input('Digite o valor de a12 '))
a20 = float(raw_input('Digite o valor de a20 '))
a21 = float(raw_input('Digite o valor de a21 '))
a22 = float(raw_input('Digite o valor de a22 '))

         
total=a00*a11*a22 + a10*a21*a02 +a20*a01*a12;
total=total+(a02*a11*a20)*-1 + (a12*a21*a00)*-1 + (a22*a01*a10)*-1;


if total!=0:
   print a00," ",a01," ",a02
   print a10," ",a11," ",a12
   print a20," ",a21," ",a22
   print "Determinante 3x3: ",total;


else:
    print "Erro "
