__author__ = 'ANDRE'
#Gerar lista de Primos
def primo(ini,fim):
    lisr = []
    lisp = []
    if ini < 2:
        ini =2
    for i in range(ini,fim):
        lisp.append(i)
        for j in lisp:
            if i % j == 0 and i!= j:
                break
            elif i % j == 0 and i == j:
                lisr.append(j)

    return lisr

print(primo(0,10000))
