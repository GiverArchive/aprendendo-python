'''
 bibliotecas externas
 PiP

tudo que faz requisição em um servidor é requisição web
Requests, get, cabeçalhos
'''

'''
import requests

buscar = None

try:
    buscar = requests.get('http://google.com') #str
    # buscar = requests.post()
    print(buscar.text)
except Exception as z:
    print(z)
'''

import requests

buscar = None
cab = {'User-agent': 'GiverOS', 'Referer': 'https://www.google.com'}
cookies = {'Ultima-visita': '10/10/2018'}
dados = {'username': 'Giver', 'password': 'senhafoda'}

try:
    buscar = requests.post('https://putsreq.com/KsTwetWYmmQwclEiaiG6', headers=cab, cookies=cookies, data=dados) #str
    # buscar = requests.post()
    print(buscar.text)
except Exception as z:
    print(z)