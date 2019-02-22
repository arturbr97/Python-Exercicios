import sys
import random
import os

nota = [None] * 6
soma = 0

for x in range(1,4):
	print(x)
	nota[x] = float(input('Nota: '))

for x in range(1,4):
	soma += nota[x]

media = soma/3

if((media>9.0)and(media<=10.0)):
	print(' A - ','Media: ',media)

elif((media>7.5)and(media<=9.0)):
	print(' B - ','Media: ',media)

elif((media>6.0)and(media<=7.5)):
	print(' C - ','Media: ',media)

elif((media>4.0)and(media<=6.0)):
	print(' D - ','Media: ',media)

elif((media<=4.0)and(media>=0)):
	print(' E - ','Media: ',media)


os.system('pause')