#
#   Project euler 21
#

def d(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

pares = []
soma = 0

for n in range(1, 10000):
    pair = d(n)
    if [pair, n] not in pares and d(n) == pair and d(pair) == n:
        pares.append([n, pair])
        soma += n + pair

print(f"Numeros amigaveis: {pares}")
print(f"Soma dos numeros amigaveis: {soma}")
