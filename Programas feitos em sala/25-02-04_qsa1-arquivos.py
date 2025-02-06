# 
# Aula de arquivos
#
#   João Gabriel 
#        04/02/2025

'''
arch = open("teste.txt", "w")
# arch =file descriptor 
#   "r" para ler   "w" para escrever (apaga o que tinha antes no arquivo)    "a" para escrever (serve para adcionar à um arquivo existente)

v1 = arch.read()# se colocar um numero no () vai ser a quantidade de bytes,1 byte = 1 caracter, que vai ler
#       Lê todo o arquivo e coloca na variavel

v2 = arch.readline()
# Lê uma linha

v3 = arch.read_lines()
# Lê todo o arquivo e gera uma lista com cada linha

arch.write("Ola mundo")
# A cada comando para ler ou escrever ele avança a posição em que o arquivo esta

arch.tell()
# Fala a posição que você está 

arch.seek()
# Tem dois parametros ("nova posição", "em relação à posição"(0 = inicial)(1 = atual)(2 = final))

arch.close()
# Fecha o arquivo
'''


'''
fd = open("x.txt", "r")
l = w = c = 0
linha = fd.readline()
while linha != "":
    c += len(linha)
    l += 1
    w += len(linha.split())
    linha = fd.readline()
fd.close()
print(l,w,c)
'''


'''
fd = open("x.txt", "r")
l = w = c = 0
for linha in fd:
    c += len(linha)
    l += 1
    w += len(linha.split())
fd.close()
print(l,w,c)
'''