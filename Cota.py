import requests
import json
import time

def cotacao():
    key = 'key'
    try:
        request = requests.get('https://api.hgbrasil.com/finance/quotations?format=json&key={}'.format(key))
        retorno = json.loads(request.text)
        return retorno
    except:
        print('Erro')

while True:
    p = dict(cotacao())
    print('\n\n\n\n\n')
    print('=== COTAÇÃO ===\n')
    print('Dolar: \t\t\tR$', p['results']['currencies']['USD']['buy'])
    print('Euro: \t\t\tR$', p['results']['currencies']['EUR']['buy'])
    print('Libra: \t\t\tR$', p['results']['currencies']['GBP']['buy'])
    print('Peso Argentino: \tR$', p['results']['currencies']['ARS']['buy'])
    print('Bitcoin: \t\tR$', p['results']['currencies']['BTC']['buy'])
    print('\n\n\n\n\n')
    time.sleep(2)