class Garrafa:


    def __init__(self, capacidade, tipoMaterial):
        self.tipoMaterial = tipoMaterial
        self.capacidade = capacidade

    def mostrarConteudo(self, tipoMaterial, capacidade):
        self.tipoMaterial= tipoMaterial
        self.capacidade = capacidade

    def encher(self):
        print("enchendo a garrafa")

    def esvaziar(self):
        print("esvaziando a garrafa")
