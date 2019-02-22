import sys
import random
import os

leia = input('Digite o Turno: ')

if(leia=='m' or leia=='M'):
	print('Bom dia !')

elif(leia=='v' or leia=='V'):
	print('Boa Tarde !')

elif(leia=='n' or leia=='N'):
	print('Boa Noite !')

os.system('pause')