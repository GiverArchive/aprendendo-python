from clientes import Cliente
from contas import Conta

Cliente1 = Cliente("Pedro Programagens", "123.123.123-12", 18)
print(Cliente1)

conta_pedrinho = Conta(Cliente1, 2000)
print(conta_pedrinho.cliente.nome)