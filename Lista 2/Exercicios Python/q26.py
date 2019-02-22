import sys
import random
import os

print('Kg de maçã')
fruta1 = float(input(': '))
print('Kg de morango')
fruta2 = float(input(': '))

valor1 = fruta1 * 2.50
valor2 = fruta2 * 1.80

print('maçã valor R$ ',valor1)
print('morango valor R$ ',valor2)

if((valor1>25) or (fruta1>8)):
	d = valor1 * 0.1
	valor1 = valor1 - d
	print('maçã desconto R$ ',valor1)

if((valor2>25) or (fruta2>8)):
	d = valor2 * 0.1
	valor2 = valor2 - d
	print('morango desconto R$ ',valor2)

os.system('pause')