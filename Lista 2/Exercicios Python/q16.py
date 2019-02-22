import sys
import random
import os
import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

delta = (b**2) - (4 * a * c)

if(delta<0):
	print('DELTA: ', delta)
	print('Não existe raízes reais! ')

else:
	x1 = (-b - math.sqrt(delta))/(2*a)
	x2 = (-b + math.sqrt(delta))/(2*a)

print('DELTA: ',delta)
print('x1: ', x1)
print('x2: ', x2)
	
os.system('pause')