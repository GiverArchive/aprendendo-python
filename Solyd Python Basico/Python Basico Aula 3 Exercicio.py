'''
Saber idade, peso e altura
ver se esta apto a entrar no exercito
minimo: 18 anos // 60 quilos // 1.70 de altura
'''
print(' \nFormulário do Exercito\n ')
idade = int(input('Qual sua idade?\nR: '))
peso = float(input('Quanto você pesa?\nR: '))
altura = float(input('Qual sua altura?\nR: '))
print(' ')
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print(' \nApto a entrar para o Exercito!!!\n ')
else:
    print(' \nNão está apto a entrar para o Exercito =(\n')