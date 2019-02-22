import sys
import random
import os

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
num3 = int(input('Num3: '))

if(num1>num2 and num2>num3):
	print(num1,'E o maior')

elif(num2>num1 and num1>num3):
	print(num2,'E o maior')

elif(num3>num2 and num2>num1):
	print(num3,'E o maior')

elif(num3>num2 and num1>num2):
	print(num3,'E o maior')


if(num1<num2 and num2<num3):
	print(num1,'E o menor')

elif(num2<num1 and num1<num3):
	print(num2,'E o menor')

elif(num3<num2 and num2<num1):
	print(num3,'E o menor')

elif(num3<num2 and num1<num2):
	print(num3,'E o menor')

os.system('pause')
