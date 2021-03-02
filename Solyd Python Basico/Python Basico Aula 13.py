'''
API - Manda parametros e retorna dados
Exemplo em OMDb

Exercicio incluido aqui neste arquivo
'''

import requests
import json

rec = None
key = 'key'


def reqfilme(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey={}&t={}&type=movie'.format(key, titulo))
        dic = json.loads(req.text)
        return dic
    except:
        print('Erro')
        return None

def print_detalhes(dic):
    print('\n')
    print('Titulo:', dic['Title'])
    print('Ano:', dic['Year'])
    print('Diretor:', dic['Director'])
    print('Autores:', dic['Actors'])
    print('Nota:', dic['imdbRating'])
    print('Premios:', dic['Awards'])
    print('Postes:', dic['Poster'])
    print('\n')

sair = False
while not sair:
    pesq = str(input('Digite o nome para pesquisa ou SAIR para sair\nR: '))
    if pesq == 'SAIR':
        print('Saindo...')
        exit()
    else:
        filme = dict(reqfilme(pesq))
        if filme['Response'] == 'False':
            print("\nFilme não encontrado!\n")
        else:
            print_detalhes(filme)