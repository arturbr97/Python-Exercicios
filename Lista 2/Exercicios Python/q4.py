import sys
import random
import os

letra = input('letra: ')

if(letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u' ):
	print('Vogal inserida')

else:
	print('Consoante(s) ou vogais')

os.system('pause')