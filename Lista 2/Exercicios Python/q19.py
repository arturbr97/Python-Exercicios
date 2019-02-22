import sys
import random
import os

num = int(input('Num: '))

centenas  = num/100
dezenas = (num%100)/10
unidades = ((num%100)%10)


print('Centenas: %.0f' % centenas)
print('Dezenas: %.1f' % dezenas)
print('Unidades: %.0f' % unidades)

os.system('pause')