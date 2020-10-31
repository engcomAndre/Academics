#coding:utf8

import os

os.system("clear")

x = input("Tamanho do lista 1: ")
y = input("\nTamanho do lista 2: ")

l1 = []
l2 = []
l3 = []

print "Digite os valores da lista 1: "
for i in range(x):
	l1.append(input())

print "Digite os valores da lista 2: "
for j in range(y):
	l2.append(input())

i=0
j=0

while i<len(l1):
	l3.append(l1[i])
	if j<len(l2):
		l3.append(l2[j])
	i+=1
	j+=1
print "A lista intercalado é: ",l3
