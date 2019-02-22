hora = float(input('Digite o Valor da sua Hora '))
qtd = float(input('Digite a quandiade de Horas trabalhadas por Mes '))

salario =  hora * qtd
print('Salario',salario)
if salario <= 900:
    
    print('ISENTO')
    
elif salario <= 1500:
    
    print('Salário Bruto ',salario)
    ir = salario * 0.05
    print('IR ',ir)
    inss = salario * 0.10
    print('INSS ',inss)
    sindicato = salario * 0.03
    print('Sindicato ', sindicato)
    total = ir + inss + sindicato
    print('Total de Descontos', total)
    salarioli =  salario - total
    print('Salario Liquido', salarioli)

elif salario <= 2500:
    
    print('Salário Bruto ',salario)
    ir = salario * 0.10
    print('IR ',ir)
    inss = salario * 0.10
    print('INSS ',inss)
    sindicato = salario * 0.03
    print('Sindicato ', sindicato)
    total = ir + inss + sindicato
    print('Total de Descontos', total)
    salarioli =  salario - total
    print('Salario Liquido', salarioli)

elif salario > 2500:
    
    print('Salário Bruto ',salario)
    ir = salario * 0.10
    print('IR ',ir)
    inss = salario * 0.20
    print('INSS ',inss)
    sindicato = salario * 0.03
    print('Sindicato ', sindicato)
    total = ir + inss + sindicato
    print('Total de Descontos', total)
    salarioli =  salario - total
    print('Salario Liquido', salarioli)
