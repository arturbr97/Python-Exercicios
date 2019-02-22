op = input('1- File Duplo 2- Alcatra 3- Picanha \n')
    
peso = float(input('Digite quantos Kg de Carne: '))

if op == 1 and peso <= 5:
     valor = peso * 4.90
     print('Valor a ser pago',valor)
elif op == 1 and peso > 5:
    valor = peso * 5.80
    print('Valor a ser pago',valor)

if op == 2 and peso <= 5:
    valor = peso * 5.90
    print('Valor a ser pago',valor)

elif op == 2 and peso > 5:
    valor = peso * 6.80
    print('Valor a ser pago',valor)

if op == 3 and peso <= 5:
    valor = peso * 6.90
    print('Valor a ser pago',valor)
elif op == 3 and peso > 5:
    valor = peso * 7.80
    print('Valor a ser pago',valor)
