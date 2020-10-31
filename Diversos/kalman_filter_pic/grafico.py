
# grafico.py
# written by Alynne Ferreira (alynneferreiras@gmail.com)

import time
import serial
import sys
import matplotlib.pyplot as plt

def main():
    arq_in = open('voltagein.txt','w')
    arq_out = open('voltageout.txt','w')
    arq_in2 = open('cannonin.txt','w')
    arq_out2 = open('cannonout.txt','w')
    
    ser = serial.Serial(
        port = '/dev/ttyUSB0', # porta pode mudar
        baudrate = 115200 # depende do baudrate do pic
    )

    print(ser.isOpen()) # 'True' se estiver aberta

    # voltage
    cont = 0
    while cont < 800:
        valor = ser.readline()
        print(valor)
        arq_in.write(str(valor.split('\t')[1])+'\n') # valor com erro
        arq_out.write(str(valor.split('\t')[2].strip('\n'))+'\n') # valor filtrado
        cont += 1
    cont = 0
    
    # cannon
    while cont < 800:
        valor = ser.readline()
        print(valor)
        arq_in2.write(str(valor.split('\t')[1])+'\n') # valor com erro
        arq_out2.write(str(valor.split('\t')[2].strip('\n'))+'\n') #valor filtrado
        cont += 1

    arq_in.close()
    arq_out.close()
  
    arq_in2.close()
    arq_out2.close()

main()