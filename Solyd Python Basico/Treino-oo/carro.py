from veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, combustivel):
        Veiculo.__init__(self, cor, 4, marca, combustivel)
    
    def abastecer(self, litros):
        if self.combustivel + litros > 50:
            print("Tanque cheio!")
        else:
            self.combustivel += litros