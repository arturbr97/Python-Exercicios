class lampada:


    def __init__(self, status):
        self.status = status


    def ligar(self, status):
        self.status = True


    def desligar(self):
        self.status= False

    def observar(self, status):
        if self.status ==  True:
            print("lampada ligada")
        else:
            print("lampada desligada")
