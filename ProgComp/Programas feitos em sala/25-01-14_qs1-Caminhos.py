'''
caminhos = [
 [75],
 [95, 64],
 [17, 47, 82],
 [18, 35, 87, 10],
 [20,  4, 82, 47, 65],
 [19,  1, 23, 75,  3, 34],
 [88,  2, 77, 73,  7, 63, 67],
 [99, 65,  4, 28,  6, 16, 70, 92],
 [41, 41, 26, 56, 83, 40, 80, 70, 33],
 [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [ 4, 62, 98, 27, 23,  0, 70, 98, 73, 93, 38, 53, 60,  0, 23]
]

ind = -1
caminho = []

x = [3, 4]
y = [5]
z = x.append(y)

print(z)
'''
'''
for linha in caminhos:
    ind += 1
    caminho.append()
    for x in caminhos: 
        '''
caminhos = [
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3]
]

for l in range(1, len(caminhos)):
    caminhos[l][0] += caminhos [l -1][0]
    for c in range(1, len(caminhos[l] -1)):
        caminhos[l][c] += max(caminhos[l -1] [c -1], caminhos[l -1][c])
    
    caminhos[l][l] += caminhos [l -1][l -1]


print(caminhos)
print(caminhos[3])
print(max(caminhos[len(caminhos) -1]))

