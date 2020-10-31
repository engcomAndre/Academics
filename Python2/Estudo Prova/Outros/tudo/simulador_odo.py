#coding:utf8

#Simular um odometro

import os
os.system("clear")

a=0
b=0
c=0
d=0
e=0
f=0

while a<9:
	b=0
	c=0
	d=0
	e=0
	f=0
	while b<9:
		c=0 
		d=0
		e=0
		f=0
		while c<9:
			d=0
			e=0
			f=0
			while d<9:
				e=0
				f=0
				while e<9:
					f=0
					while f<9:
						os.system("clear")	
						print a,b,":",c,d,":",e,f
						if a==9:
							a=0
							b=0
							c=0
							d=0
							e=0
							f=0	
						f+=1
					e+=1
				d+=1
			c+=1
		b+=1
	a+=1
