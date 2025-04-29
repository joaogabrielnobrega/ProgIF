##teste

l= [15, 42, 30]
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

'''


#print(l)
#print(str(l))

soma = lambda d: d+3

print(soma(3,5))

print(list(map(soma, a)))

print(map(soma, a))

g = map(soma, a)

print(g)

for x in map(soma, a):
    print(x)

'''

import functools

ultimo = lambda d, f: d + f

#a = ["1", "2", "3", "4"]
print(list(functools.reduce(ultimo, a, b)))


#print(list(reduce(ultimo, a)))

par = lambda x: x % 2 == 0

#print(list(filter(par, a)))


'''
l = [["Gio", 20], ["zi", 31], ["Ti", 33]]
l1 = sorted(l)
l2 = sorted(l, key = lambda x: x[1])
l3 = sorted(l, key = lambda x: x[1])
print(l1)
print(l2)
print(l3)
'''