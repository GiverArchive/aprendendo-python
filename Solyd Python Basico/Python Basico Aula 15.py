import requests
import json
import time
import re

#Cotação

def cotacao():
    key = 'key'
    try:
        request = requests.get('https://api.hgbrasil.com/finance/quotations?format=json&key={}'.format(key))
        retorno = json.loads(request.text)
        return retorno
    except:
        print('Erro')

sair = False
while not sair:
    p = dict(cotacao())
    print('\n\n\n\n\n')
    print('=== COTAÇÃO ===\n')
    print('Dolar: \t\t\tR$', re.search(r'\w+\.\w\w', str(p['results']['currencies']['USD']['buy'])).group())
    print('Euro: \t\t\tR$', re.search(r'\w+\.\w\w', str(p['results']['currencies']['EUR']['buy'])).group())
    print('Libra: \t\t\tR$', re.search(r'\w+\.\w\w', str(p['results']['currencies']['GBP']['buy'])).group())
    print('Peso Argentino: \tR$', re.search(r'\w+\.\w\w', str(p['results']['currencies']['ARS']['buy'])).group())
    print('Bitcoin: \t\tR$', re.search(r'\w+\.\w\w', str(p['results']['currencies']['BTC']['buy'])).group())
    print('\n\n\n\n\n')
    time.sleep(2)

#Clima
'''
def clima():
    key = 'key'
    cidade = input("Qual sua cidade?\nR: ")
    try:
        requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(cidade, key))
        tempo = json.loads(requisicao.text)
        print("Tempo")
        print("Condição:", tempo['weather'][0]['main'])
        print("Temperatura:", float(tempo['main']['temp']) - 273.15)
    except:
        print('Erro')
clima()
'''