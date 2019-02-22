import sys
import random
import os

# 1 Faça um programa que peça dois numeros e imprima o maior deles

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))

if(num1>num2):
	print(num1,'>',num2)

elif(num2>num1):
	print(num2,'>',num1)


os.system('pause')