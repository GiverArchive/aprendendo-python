###########################
#Calcular função em Python#
###########################

calculos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for calculo in calculos:
    print('=== Calcular função de X ===')
    print('Sessão', calculo)
    print(' ')
    a = input('Qual o valor individual?\nR: ')	
    b = input('Qual o valor fixo?\nR: ')
    var = input('Qual a variavel (X)?\nR: ')
    calc = int(a) * int(var)
    fx = calc + int(b)
    print(' ')
    print('Aguarde enquanto calculo pra você!!\nRelaxa, pode ir tomando seu café!')
    print('Pera, pera, não da tempo de tomar café, ja calculei\n.')
    print('O valor total é:', fx)
    print(' \nViu como eu calculo rápido???\n')
    print('================')