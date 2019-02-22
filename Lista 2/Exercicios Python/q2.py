import sys
import random
import os

valor = int(input('Num: '))

if(valor>0):
	print('Valor positivo')

elif(valor<0):
	print('Valor negativo')

elif(valor==0):
	print('Valor nulo')

else:
	print('Valor invalido')

os.system('pause')