'''
Usar argumentos para passar coisas
Bibioteca sys
Import <lib>
'''
'''
import sys
argumentos = sys.argv
print(argumentos)
'''
'''
argumento é tudo o que é passado para a linguagem
SYS faz com que o programa use o SO
'''
import sys

argumentos = sys.argv #Arg0 METODO // Arg1 n1 // arg2 n2

def soma(n1, n2):
    return float(n1) + float(n2)
	
def sub(n1, n2):
    return float(n1) - float(n2)

if argumentos[1] == "soma":
    resp = soma(argumentos[2], argumentos[3])
elif argumentos[1] == "sub":
    resp = sub(argumentos[2], argumentos[3])
print(resp)
'''
fim da aula
'''