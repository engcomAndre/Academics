__author__ = 'ANDRE'

import time
import os # Biblioteca de funcoes do sistema operacional
#os.system("clear") # No linux ou mac os
os.system("cls") # No windows, wince, nt
i = 0
while i < 24:
        j = 0
        while j < 60:
                k = 0
                while k < 60:
                        os.system("cls")
                        print( i,":",j,":",k)
                        k = k + 1
                        time.sleep(1)
                j = j + 1
        i = i + 1

# fim do programa



