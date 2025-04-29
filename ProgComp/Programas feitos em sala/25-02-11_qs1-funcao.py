#
#   Project euler 21
#
import datetime

def d(n):
    soma = 1
    for i in range(2, n //2 +1):
        if n % i == 0 :
            soma += i
    return soma

start = datetime.datetime.now()
soma = 0

for n in range(1, 10000):
    pair = d(n)
    if d(pair) == n and n != pair:
        soma += n

print(f"Soma dos numeros amigaveis: {soma}")

end = datetime.datetime.now()
print(end - start)