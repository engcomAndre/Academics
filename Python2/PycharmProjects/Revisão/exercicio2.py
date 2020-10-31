__author__ = 'ANDRE'
#coding = 1252

def pro (a):
    if a < 10:
        print(a)
        a += 1
        pro(a)

pro(0)