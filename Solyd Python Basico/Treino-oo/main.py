from veiculos import Veiculo
from carro import Carro

van = Veiculo('verde', 4, 'volvo', 50)
kombosa = Veiculo('rip', 4, 'volkswagem', 52)
uno_de_firma = Carro('branco', 'fiat', 30)

print("\n-= Van =-")
print("> Cor:", van.cor)
print("> Rodas:", van.rodas)
print("> Marca:", van.marca)
print("> Tanque:", van.combustivel)

print("\n-= Kombosa =-")
print("> Cor:", kombosa.cor)
print("> Rodas:", kombosa.rodas)
print("> Marca:", kombosa.marca)
print("> Tanque:", kombosa.combustivel)
kombosa.abastecer(12)
print("Novo Tanque:", kombosa.combustivel)

print("\n-= Uno de Firma =-")
print("> Cor:", uno_de_firma.cor)
print("> Rodas:", uno_de_firma.rodas)
print("> Marca:", uno_de_firma.marca)
print("> Tanque:", uno_de_firma.combustivel)
uno_de_firma.abastecer(12)
print("Novo Tanque:", uno_de_firma.combustivel)
uno_de_firma.abastecer(30)
print("Novo Tanque:", uno_de_firma.combustivel)