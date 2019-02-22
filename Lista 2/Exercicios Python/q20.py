import sys
import random
import os

num = int(input('Valor do saque: '))

centenas  = num/100
dezenas = (num%100)/10
unidades = ((num%100)%10)

if(centenas>0):
	print('%.0f' % centenas,' Nota(s) de R$ 100')

if(dezenas<5):
	print('%.0f' % dezenas,' Nota(s) de R$ 10')

elif((dezenas>=5) or (dezenas<=9)):
	print('1 Nota de 50')
	print('%.0f' % dezenas-5,' Nota(s) de R$ 10')
	
if(unidades==2):
	print('1 Nota de R$ 2')

elif(unidades==4):
	print('2 Nota de R$ 2')

elif(unidades==7):
	print('1 nota de R$ 5 e 1 de R$ 2')

elif(unidades==9):
	print('1 nota de R$ 5 e 2 de R$ 2')

print('Valor do Saque R$ ',num)

if((unidades==1)or(unidades==5)):
	os.system('cls')
	print('Cedulas não disponiveis para quantia informada!')

os.system('pause')