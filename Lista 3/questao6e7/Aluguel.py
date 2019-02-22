class aluguel:

    def __init__(self, marcaCarro, modeloCarro, valorDiaria, quantDiarias):
        self.marcaCarro = marcaCarro
        self.modeloCarro = modeloCarro
        self.valorDiaria = valorDiaria
        self.quantDiarias = quantDiarias

    def mostrarAluguel(self):
        print('Marca do Carro {}, Modelo do carro é {}, Valor da Diaria é {}, e Quantidade de Diarias é {}'.format(self.marcaCarro, self.modeloCarro, self.valorDiaria , self.quantDiarias ))

    def valorPago(self):
        a = self.valorDiaria * self.quantDiarias
        print('Valor a pagar: {} '.format(a) )

