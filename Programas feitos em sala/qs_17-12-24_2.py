#variancia = (((num1 - media) ** 2) + ((num2 - media) ** 2) + ((num3 - media) ** 2))/ (nnum - 1)

#desvio padrão = variancia ** 0,5

#Problema para aprender lista
#função variavel.append() adciona um elemento a uma lista

numeros = []
soma = 0
qtde = 0
num = int(input())
while num >= 0:
    soma += num
    qtde += 1
    numeros.append(num)
    num = int(input())
#Proteger com if qtde >= 1:
media = soma / qtde
dp = 0
for num in numeros:
    dp += (num - media) ** 2
dp /= qtde - 1
print(dp)