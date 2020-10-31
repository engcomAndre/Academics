#coding:utf8
#programa pra verficar se um numero é primo.

x = int(input("Digite x: "))
div=1
i=0
while div <= x:
	if(x%div==0):
		i+=1
	div+=1
if(i==2):
	print u" é primo!!!"
else:
	print u"não é primo!!!"



