'''
Estruturas de laço
Percorrem uma coleção de valores
FOR e WHILE

nomes = ['Joca', 'Marcos', 'Kilto', 'Spii', 'Giver']
for nome in nomes:
    print(nome)
	
lista_numeros = range
'''
'''
lista_numeros = range(25)
for numero in lista_numeros:
    print(numero)
'''
	
'''
range(5, 10)
especifica o intervalo
range(5, 100, 2)
especifica intervalo entre proximo items
'''
'''
lista =  range(5, 40, 3)
for i in lista:
    print(i)
'''
'''
listanova = ['KILL', 'ban', 'meliodas', 'hill', 'climb']
for i in range(5):
    print(listanova[i])
'''
'''
listanova = ['KILL', 'ban', 'meliodas', 'hill', 'climb']
for i in range(len(listanova)):
    print(listanova[i])
	'''
'''
WHILE - Enquanto

enquanto o valor retonar True, em boolean, executara cada item novamente
'''
'''
import socket
site = str(input('Em que site deseja se conectar?\nR:'))
tentativas = int(input('Quantas vezes deseja tentar se conectar\nR: '))
maximo = tentativas
minimo = 1
print('Tentando', tentativas, 'vezes')
while minimo <= maximo:
    print('Tentativa', minimo)
    ten = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ten.settimeout(0.25)
    cod = ten.connect_ex((site, 80))
    if cod == 0:
        print('Sucesso na tentativa', minimo)
        minimo = minimo + tentativas
    else:
        print('Erro na tentativa', minimo)
    minimo = minimo + 1
'''
'''
frutas = ['limao', 'pera', 'abacaxi', 'maçã', 'manga', 'acerola']
contador = 0
for fruta in frutas:
    contador += 1
    print(contador)    

print(len(frutas))
'''
'''
numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
	
'''





















