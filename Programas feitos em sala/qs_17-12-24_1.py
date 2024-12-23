try:
    num = int(input("Digite um numero maior que 0: \n"))
except:
    num = int(input("Digite um NUMERO VALIDO maior que 0: \n"))

soma = 0
quantidade_numeros = 0

while num >= 0:
    soma += num
    quantidade_numeros += 1
    try:
        num = int(input("Caso queira parar a soma digite um numero menor que zero, pelo contrario digite um numero maior que 0: \n"))
    except:
        num = int(input("Caso queira parar a soma digite um NUMERO VALIDO menor que zero, pelo contrario Digite um NUMERO VALIDO maior que 0: \n")) 

print("Essa é a soma dos numeros digitados: ", soma)
print("quantidade elementos", quantidade_numeros)

if quantidade_numeros > 0:
    media_aritimetica = soma / quantidade_numeros
    print("Media", media_aritimetica)
else:
    print("Nenhum numero")
#