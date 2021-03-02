#Calculadora

#Intro#
print(' ')
print('Calculadora')
print(' ')
#Seleção#
print('Qual operação deseja fazer?\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação')
calculo = input('R: ')
print(' ')
#Calculos#
if calculo == '1':
    print(' \nAdição\n ')
    a1 = input('Qual o primeiro numero?\nR: ')
    a2 = input('Qual o segundo numero?\nR: ')
    print('O resultado é:')
    print(' ', float(a1) + float(a2))
    print(' ')
elif calculo == '2':
    print(' \nSubtração\n ')
    b1 = input('Qual o primeiro numero?\nR: ')
    b2 = input('Qual o segundo numero?\nR: ')
    print('O resultado é:')
    print(' ', float(b1) - float(b2))
    print(' ')
elif calculo == '3':
    print(' \nDivisão\n ')
    c1 = input('Qual o primeiro numero?\nR: ')
    c2 = input('Qual o segundo numero?\nR: ')
    print('O resultado é:')
    print(' ', float(b1) / float(b2))
    print(' ')
elif calculo == '4':
    print(' \nMultiplicação\n ')
    d1 = input('Qual o primeiro numero?\nR: ')
    d2 = input('Qual o segundo numero?\nR: ')
    print('O resultado é:')
    print(' ', float(d1) * float(d2))
    print(' ')
else:
    print(' \nOpção invalida\n')