from clientes import Cliente

class Conta(Cliente):
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
    
    def sacar(self, quantia):
        if self.saldo - quantia < 200:
            print("Conta sem fundos!")
        else:
            self.saldo -= quantia
            print("Sacou", quantia, "reais!")
    
    def depositar(self, quantia):
        if self.saldo + quantia > 50000:
            print("Limite atingido!")
        else:
            self.saldo += quantia
            print("Depositado", quantia, "reais!")