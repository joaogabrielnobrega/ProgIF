l = [2, 4, 7, 20, 27, 36, 40]
elemento = 0
l1= [] 

while elemento < len(l) - 1:
    l1 += [l[elemento] + l[elemento + 1]]
    elemento += 1
#l2 = [l[elemento] + l[elemento + 1] for elemento in l]
print (l1)

