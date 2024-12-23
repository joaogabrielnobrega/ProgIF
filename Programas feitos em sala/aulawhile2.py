#codigo para calcular media simples

qtde_num = 0
soma = 0
num = int(input("Insira o numero: "))

while num >= 0:
    soma = soma + num
    qtde_num = qtde_num + 1
    num = int(input("Insira o numero, para parar o codigo insira um numero negativo: "))
if qtde_num > 0:
    print(f"a media é : {soma/qtde_num}")
else: 
    print("Impossivel calcular media")