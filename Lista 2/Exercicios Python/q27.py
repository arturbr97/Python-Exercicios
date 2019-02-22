import sys
import random
import os

print('\n1 - File Duplo \n2 - Alcatra \n3 - Picanha')

carn = input(': ')

if(carn=='1'):
	print('File Duplo em Kg ')
	carn1 = float(input(': '))
	carn1 = carn1 * 4.90
	print('Valor R$: ',carn1)

if(carn=='2'):
	print('Alcatra em Kg ')
	carn2 = float(input(': '))
	carn2 = carn2 * 5.90
	print('Valor R$: ',carn2)

if(carn=='3'):
	print('Picanha em Kg ')
	carn3 = float(input(': '))
	carn3 = carn3 * 6.90
	print('Valor R$: ',carn3)

os.system('pause')