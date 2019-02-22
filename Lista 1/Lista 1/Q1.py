#Faça um Programa que peça dois números e imprima o maior deles.

n1 = input('Digite o primero numero: ')
n2 = input('Digite o segundo numero: ')

if n1 > n2:
    print (n1,'é maior que',n2)
elif n2 > n1:
    print (n2,'é maior que',n1)
else: #caso não seja if e nem elif 
    print( 'os numeros são iguais')
