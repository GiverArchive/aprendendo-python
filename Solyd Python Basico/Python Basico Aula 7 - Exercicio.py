'''
Faça uma função que recebe valores de uma coleçao e retorna o maior
E uma função que retorna o menor
'''

def maior(colect):
    resp = max(colect)
    return resp
def menor(colect):
    resp = min(colect)
    return resp

lista = [4, 6, 2, 7, 13, 5]

print('O maior valor é', maior(lista), '\nE o menor valor é', menor(lista))


'''
ou
'''

def maior_item(colecao):
    maior_item2 = colecao[0]
    for item in colecao:
        if item > maior_item2:
            maior_item2 = item
    return maior_item2

def menor_item2(colecao):
    menor_item2 = colecao[0]
    for item in colecao:
        if item < menor_item2:
            menor_item2 = item
    return menor_item2

print(menor([1,-2,1.2,87.2,1289,-7,0]))