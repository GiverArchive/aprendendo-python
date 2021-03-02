open('entrada.txt') #abre
open('C:\\dir1\\dir2\\arquivo.txt') # abre
open('entrada.txt',  'w')# modo Write
open('entrada.txt', 'r') # modo read
open('arquivo.txt', 'r+') #Modo leitura e escrita
open('entrada.txt', 'a') # modo append
open('a.ext', 'b') #modo de arquivos que são diferentes de texto

arquivo = open('arquivo.txt', 'w')
arquivo.write("come batata")

for i in range(1, 200):
    arquivo.write(i)

arquivo = open('arquivo.txt', 'r')
print(arquivo.read())
for linha in arquivo:
    print(linha)

a = open('entry.png', 'b')

a = open('entry.png', 'rb')
print(a.read())