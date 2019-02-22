import sys
import random
import os

n1 = float(input('N1: '))
n2 = float(input('N2: '))

op = input('operacao + - * /: ')

x = n1+n2

if(op=='+'):
	r = n1+n2
	print('= ',n1+n2)

elif(op=='-'):
	r = n1-n2
	print('= ',n1-n2)

elif(op=='*'):
	r = n1*n2
	print('= ',n1*n2)

elif(op=='/'):
	r = n1/n2
	print('= ',n1/n2)


if(r>0):
	print(r,' e positivo')
elif(r<0):
	print(r,' e negativo')
elif(r==0):
	print(r,' e nulo')
if(r%2==0):
	print(r,'e par')
elif(r%2!=0):
	print(r,'e impar')
if isinstance(x, int):
	print(r,'e um inteiro...')
else:
	print(r,' não é inteiro...')
	
os.system('pause')