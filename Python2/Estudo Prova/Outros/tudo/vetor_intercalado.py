#coding:utf8

#Criar um vetor com valores intercalados de outros dois vetores...

import os

os.system("clear")

x = input("Tamanho do vetor 1: ")
y = input("\nTamanho do vetor 2: ")

v1 = []
v2 = []
v3 = []

print "Digite os valore do vetor 1: "
for i in range(x):
	v1.append(input())

print "Digite os valore do vetor 2: "
for j in range(y):
	v2.append(input())

i=0
j=0

while i<len(v1):
	v3.append(v1[i])
	if j<len(v2):
		v3.append(v2[j])

	i+=1
	j+=1
print "O vetor intercalado é: ",v3
