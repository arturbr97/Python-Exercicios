import sys
import random
import os

valor = input('Valor: ')

if(valor=='1'):
	print('Domingo')

elif(valor=='2'):
	print('Segunda-Feira')

elif(valor=='3'):
	print('Terça-Feira')

elif(valor=='4'):
	print('Quarta-Feira')

elif(valor=='5'):
	print('Quinta-Feira')

elif(valor=='6'):
	print('Sexta-Feira')

elif(valor=='7'):
	print('Sábado')

else:
	print('Valor invalido!')

os.system('pause')