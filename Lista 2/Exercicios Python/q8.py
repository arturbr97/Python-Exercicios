import sys
import random
import os



val1 = float(input('Preco do Sabao em pó: '))
val2 = float(input('Preco do Sabonete: '))
val3 = float(input('Preco do Sabao de barra: '))

if(val1<val2 and val2<val3):
	print('R$',val1,'Preco do Sabao em pó eo mais barato !')

elif(val2<val1 and val1<val3):
	print('R$',val2,'Preco do Sabonete eo mais barato ')

elif(val3<val2 and val2<val1):
	print('R$',val3,'Preco do Sabao de barra eo mais barato !')

elif(val3<val2 and val1<val2):
	print('R$',val3,'Preco do Sabao de barra eo mais barato !')

print('\n')
os.system('pause')