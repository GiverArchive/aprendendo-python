'''
No que ha parenteses, é função

print(obj)
print(len(obj))

o que fica no paranteses é paramentro
print(parametro)

para definir uma função, usa-se a palavra 'def'
'''
def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(12, 24)

print(retorno)

'''
A função precisa ter retorno:
'''
def printaoi():
    print("OIE")

printaoi()

'''
hehe
'''
def tem_sete_itens(par):
    if len(par) == 7:
        return True
    else:
        return False

if tem_sete_itens("palavra"):
    print("Sim, tem 7 itens")
else:
    print("É, não tem 7 itens")

'''
Metodos nao tem retorno
'''