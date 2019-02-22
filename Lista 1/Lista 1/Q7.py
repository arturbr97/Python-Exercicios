# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite o 1 numero: '))
n2 = float(input('Digite o 2 numero: '))
n3 = float(input('Digite o 3 numero: '))
def maior():
if n1 > n2 and n1 > n3:
    print('O maior Valor e ',n1)
elif n2 > n1 and n2 > n3:
    print('O maior Valor e ', n2)
elif n3 > n1 and n3 > n2:
    print('O maior Valor e ', n3)
def menor():
    
if n1 < n2 and n1 < n3:
    print('O menor Valor e ',n1)
elif n2 < n1 and n2 < n3:
    print('O menor Valor e ', n2)
elif n3 < n1 and n3 < n2:
    print('O menor Valor e ', n3)

maior()   
menor()
