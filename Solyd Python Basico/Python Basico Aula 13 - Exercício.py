#execicios
import requests
import json

key = 'key'

def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            print('Pesquisando em página ' + i)
            req = requests.get('http://www.omdbapi.com/?apikey={}&type=movie&s={}&page={}'.format(key, titulo, str(i)))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    titulo2 = filme['Title']
                    ano = filme['Year']
                    string = titulo2 + ' (' + ano + ')'
                    lista.append(string)
            else:
                print('Fim')
                break
        except:
            print('\nFalha\n')
            return lista
    return lista

sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR\nR: ')
    if op == 'SAIR':
        print('\nSaindo...')
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('\nEncontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print('\n', filme)
        print('\nFim')


