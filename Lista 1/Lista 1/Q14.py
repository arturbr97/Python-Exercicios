nota1 = float(input('Digite a 1 nota: '))
nota2 = float(input('Digite a 1 nota: '))
nota3 = float(input('Digite a 1 nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 9 and media <= 10:
    print('Conceito A')
elif media >= 7.5 and media < 9.0:
    print('Conceito B')
elif media >= 6 and media < 7.5:
    print('Conceito C')
elif media >= 4 and media < 6:
    print('Conceito D')
else :
    print('Conceito E')
