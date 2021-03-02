'''
Padrões -- Expressões Regulares
Email = user@dominio.ext
Telefone DDD 9 NUME NUME
IP = 255.255.255.255
'''
import re
import requests

teste = 'O gato é bonito'
padrao = re.search(r'gat\w', teste) # RAW STRING =- Sem caractere especial (r'str') // . = * // \w
if padrao:
    print(padrao.group()) # >> gato
else:
    print('Nao encontrado')

gatos = 'O gato, a gata, os gatinhos, os gatoes'
padr = re.findall(r'gat\w', gatos) # Todas as incidencias // lista
if padr:
    print(padr)
else:
    print('Nao encontrado')

gatosos = 'O gato, a gata, os gatinhos, os gatoes'
padro = re.findall(r'gat\w+', gatosos) # Todas as incidencias // indefinidamente \w* 0 ou mais apos a letra padronizada
if padr:
    print(padro)
else:
    print('Nao encontrado')

frase = 'O gato, a gata, os gatinhos, os gatoes'
grupo = re.findall(r'[gat]+', frase) # dxd   a{3} = aaa
if padr:
    print(grupo)
else:
    print('Nao encontrado')
    
email = requests.get('www.google.com')
achador = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', email.text)
print(achador)