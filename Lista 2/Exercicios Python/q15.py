import sys
import random
import os

l1 = int(input('L1: '))
l2 = int(input('L2: '))
l3 = int(input('L3: '))

if((l1==l2) and (l2==l3)):
	print('Triangulo Equilatero')

elif((l1==l2) or (l2==l3) or (l1==l3)):
	print('Triangulo Isosceles')

else:
	print('Triangulo Escaleno')

os.system('pause')