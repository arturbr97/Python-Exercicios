import sys
import random
import os

ano = int(input('Ano: '))

if(ano % 4 == 0 && (ano % 400 == 0 || ano % 100 != 0)):
	print('\n Ano bissexto.')

else:
	print('\n Ano nao bissexto')
	
os.system('pause')