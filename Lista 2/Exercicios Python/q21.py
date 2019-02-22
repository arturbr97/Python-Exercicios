import sys
import random
import os


x = 12

if isinstance(x, int):
	print(x,'e um inteiro...')

else:
	print(x,' não é inteiro...')

if(x % 2 == 0):
	print(x,'e par...')
	
os.system('pause')