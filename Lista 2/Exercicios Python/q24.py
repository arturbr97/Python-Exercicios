import sys
import random
import os

print('Responda S(sim) ou N(não)...')

print ("Telefonou para a vítima?")
r1 = input(': ')
print ("Esteve no local do crime?")
r2 = input(': ')
print ("Mora perto da vítima?")
r3 = input(': ')
print ("Devia para a vítima?")
r4 = input(': ')
print ("Já trabalhou com a vítima?")
r5 = input(': ')

rx = 0

if(r1=='S'):
	rx += 1

if(r2=='S'):
	rx += 1

if(r3=='S'):
	rx += 1

if(r4=='S'):
	rx += 1

if(r5=='S'):
	rx += 1

if(rx==2):
	print('Suspeito')

elif((rx>=3) and (rx<=4)):
	print('Cumplice')

elif(rx>=5):
	print('Assasino')

else:
	print('Inocente')

os.system('pause')