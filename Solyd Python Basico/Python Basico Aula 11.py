import time

try:
    a = 10/0
except:
    print('deu merda')

try:
    a = 10/0
except ZeroDivisionError:
    print('deu merda')
except NameError:
    print('ta errado!')

except Exception as erro:
    print("Erro: " erro)

def abre_arquivo():
    open('arquivo.txt')
try:
    abre_arquivo()
except Exception as sx:
    print(sx)
    time.sleep(5)
	abre_arquivo()
print('aew')

def abrir():
    try:
        open("a.txt")
        return True
    except Exception as ex:
        print(ex)
        return False
while not abrir():
    print('Finnaly')
print('ae')