class Veiculo:
    def __init__(self, cor, rodas, marca, combustivel):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, litros):
        self.combustivel += litros
