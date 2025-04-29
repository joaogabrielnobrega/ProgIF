l = [2, 4, 7, 20, 27, 36, 40]

l1= [(l[0]+ l[1]), (l[1]+ l[2]), (l[2]+ l[3]),.... ] #Isso é oq ele quer

## diferença do append e +, *
l = [[1, 2], 3, 4]
l2 = l.append(5,6)
l3 = l + [5,6]
l4 = [5, 6] + l
l5 = [l+[5,6]]

## LER SLIDES DE LISTAS

#Função pega o maior numero da lista
max(lista)

#Função pega o menor numero da lista
min(lista)

#Função para somar numeros da lista
sum(lista)

n = range(101)
sumnp = sum(n[::2])
print(n[::2])
print(sumnp)

###

## função importante para lista
#Função "  SPLIT   " 

#Ex1:
filha = "Zi Batista Souza"
nomes = filhas.split() ##["Zi", "Batista", "Souza"]
print(nomes)

#Ex2:
nomes = filha.split('t') ##["Zi Ba", "is", "a Sousa"]
print(nomes)

#Teste1:
print(filha.split()) ##O Que o core

#comprehensions

#Ex1; 
idades = [52, 29, 27, 17]
idades202x = [idade+1 for idade in idades]
S = [x**2 for x in range(20)]
K = [x//1024 for x in S if x % 1024 == 0]

#Ex2;
l = ["juliana", "jose", "julio", "maria", "kaylane"]
print([n.upper() for n in l])
