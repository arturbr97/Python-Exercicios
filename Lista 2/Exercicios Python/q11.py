import sys
import random
import os

salario = float(input('Valor do Salario: '))

if(salario<=280):
	print('Salario antes do reajuste: R$ ', salario)
	print('Aumento de 20%')
	print('Valor do aumento: R$ ', (salario*0.20))
	print('Salario com Reajuste: R$ ', (salario*0.20)+salario)

elif((salario>280)and(salario<=700)):
	print('Salario antes do reajuste: R$ ', salario)
	print('Aumento de 15%')
	print('Valor do aumento: R$ ', (salario*0.15))
	print('Salario com Reajuste: R$ ', (salario*0.15)+salario)

elif((salario>700)and(salario<=1500)):
	print('Salario antes do reajuste: R$ ', salario)
	print('Aumento de 10%')
	print('Valor do aumento: R$ ', (salario*0.10))
	print('Salario com Reajuste: R$ ', (salario*0.10)+salario)

elif(salario>1500):
	print('Salario antes do reajuste: R$ ', salario)
	print('Aumento de 5%')
	print('Valor do aumento: R$ ', (salario*0.05))
	print('Salario com Reajuste: R$ ', (salario*0.05)+salario)

print('\n')
os.system('pause')