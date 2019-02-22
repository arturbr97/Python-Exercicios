#Faça um programa que pergunte o preço de três produtos e informe
#qual produto você deve comprar, sabendo que a
#decisão é sempre pelo mais barato.

preco1 = float(input('Digite o Preco do 1 produto '))
preco2 =  float(input('Digite o preco do 2 produto '))
preco3 =  float(input('Digite o preco do 3 produto '))

if preco1 < preco2 and preco1 < preco3:
    print('Menor valor e ',preco1)
elif preco2 < preco1 and preco2 < preco3:
    print('Menor valor e ',preco2)
else :
    print('Menor valor e',preco3)
