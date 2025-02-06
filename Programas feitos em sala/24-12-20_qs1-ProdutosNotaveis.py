## Produtos notaveis

'''
(a + b) ** 0 = 1
(a + b) ** 1 = 1a + 1b
(a + b) ** 2 = 1a ** 2 + 2 *a * b + 1 * b ** 2
(a + b) ** 3 = 1 * a ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2 + 1 * b **3
(a + b) ** 4 = 1 * a ** 4 + 4 * a ** 3 * b + 6 * a ** 2 * b ** 2 + 4 * a * b ** 3 + 1 * b ** 4

1
1ab^0 + 1a^0b
1a^2b^0 + 2a^1b^1 + 1a^0b^2
1a^3b^0 + 3a^2b^1 + 3a^1b^2 + 1a^0b^3
1a^4b^0 + 4a^3b^1 + 6a^2b^2 + 4a^1b^3 + 1a^0b^4

'''

# programa q mostra as 10 primeiras linhas da piramide de pascal

linha_i = [1, 1]
p_linha = [1, 1]
linha = 2
linhas = [[1], [1, 1]]
linha_desejada = int(input('Qual linha você quer?'))
ultima_linha = int(input('Até qual linha você quer?'))

while linha < ultima_linha:
    elemento1 = 0
    elemento2 = 1
    while elemento2 < len(linha_i):
        elemento = linha_i[elemento1] + linha_i[elemento2]
        p_linha.insert(elemento2, elemento)
        elemento1 += 1
        elemento2 += 1
    linhas.append(p_linha)
    linha_i = p_linha
    p_linha = [1, 1]
    linha += 1

print(len(linhas))
item = 1307504
linha_24 = linhas[9]
print(linha_24)


#ultPos = -1
#for pos in range(len(linha_24))
#    if pos == 

#for item in linha_24:
#    print(item)

#linha_24 = linhas[23].find(1307504, (len(linhas[23])/2)) 
#print(linha_24)

#print(linhas)
#print(linhas[linha_desejada - 1])
#print(linha_i)
