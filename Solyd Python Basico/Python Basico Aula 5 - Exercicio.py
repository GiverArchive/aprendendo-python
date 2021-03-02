'''
Fassa um programa que pergunte o numero de convidados para uma festa
Apos, pergunte o nome da cada um dos convidadas
Apos, imprima o nome de cada um
'''
convidados = int(input('Quantas pessoas serão convidadas para a festa?\nR: '))
contador = 1
pessoas = []
while contador <= convidados:
    pessoa = input(' \nQuem vai convidar agora? #' + str(contador) + ' \nR: ')
    pessoas.append(pessoa)
    contador += 1
    print ('Convidou', pessoa, ' \n ')
print('Número máximo de convidados atingido! Serão ' +  str(len(pessoas)) + ' Convidados:')
for i in pessoas:
    print(' -', i)