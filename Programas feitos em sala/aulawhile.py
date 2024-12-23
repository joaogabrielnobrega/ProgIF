#codigo para saber quantidade de numeros primos entre 1 e 100
x = 1
npri = 0
prim = ""

while x <= 100:
    ndiv = 0
    div = 1
    while div <= x:
        if x % div == 0:
            ndiv = ndiv + 1
        div = div + 1
    if ndiv == 2:
        npri = npri + 1
        prim = prim + f", {x}" 
    x = x + 1

print(f"O numero de primos entre 1 e 100 é {npri}")
print(f"O numeros primos entre 1 e 100 são: {prim}")