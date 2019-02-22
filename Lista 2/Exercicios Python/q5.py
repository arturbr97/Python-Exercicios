import sys
import random
import os

nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))

if((nota1+nota2)/2>=7 and (nota1+nota2)/2<10):
	print(' Aprovado !')

if((nota1+nota2)/2==10):
	print(' Aprovado com distinção !')

elif((nota1+nota2)/2<7):
	print(' Reprovado !')

os.system('pause')