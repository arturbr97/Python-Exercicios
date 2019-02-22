salario = float(input('Digite seu Salario '))

if salario <= 280:
    print('Salario Antes do Reajuste ', salario)
    salario1 = salario * 1.20
    print('Percentual de Aumento 20% ')
    vlr = salario1 - salario
    print('Valor do Aumento',vlr)
    print('Salario Apos Reajuste ', salario1)
elif salario > 280 and salario <= 700:
    print('Salario Antes do Reajuste ', salario)
    salario1 = salario * 1.15
    print('Percentual de Aumento 15% ')
    vlr = salario1 - salario
    print('Valor do Aumento',vlr)
    print('Salario Apos Reajuste ', salario1)

elif salario > 700 and salario <= 1500:
    print('Salario Antes do Reajuste ', salario)
    salario1 = salario * 1.10
    print('Percentual de Aumento 10% ')
    vlr = salario1 - salario
    print('Valor do Aumento',vlr)
    print('Salario Apos Reajuste ', salario1)

elif salario > 1500:
    print('Salario Antes do Reajuste ', salario)
    salario1 = salario * 1.05
    print('Percentual de Aumento 5% ')
    vlr = salario1 - salario
    print('Valor do Aumento',vlr)
    print('Salario Apos Reajuste ', salario1)
