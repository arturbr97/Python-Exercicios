from Aluguel import aluguel

marca = str(input('qual a marca do carro:'))
modelo = str(input('qual o modelo do carro:'))
valDiaria = float(input('qual o valor da diaria:'))
quantDiaria = int(input('qual a quantidade de diarias'))

aluguel1 = aluguel(marca, modelo, valDiaria, quantDiaria)

aluguel1.mostrarAluguel()

aluguel1.valorPago()