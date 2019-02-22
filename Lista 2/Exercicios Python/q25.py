import sys
import random
import os

print('A(Alcool) ou G(Gasolina)')
comb = input(': ')

if(comb=='A'):
	print('Quantidade de Alcool: ')
	alc = float(input(': '))
	preco = alc * 4.39
	print('Valor R$ %.2f' % preco)
	if((alc>0) or (alc<=20)):
		d = preco * 0.3
		preco = preco - d
		print('Desconto R$ %.2f' % preco)
	elif(alc>20):
		d = preco * 0.5
		preco = preco - d
		print('Desconto R$ %.2f' % preco)

if(comb=='G'):
	print('Quantidade de Gasolina: ')
	gas = float(input(': '))
	preco = gas * 3.45
	print('Valor R$ %.2f' % preco)
	if((gas>0) or (gas<=20)):
		d = preco * 0.4
		preco = preco - d
		print('Desconto R$ %.2f' % preco)
	elif(gas>20):
		d = preco * 0.6
		preco = preco - d
		print('Desconto R$ %.2f' % preco)
	
os.system('pause')