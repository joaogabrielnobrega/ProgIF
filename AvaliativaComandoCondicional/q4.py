#Codigo para descobrir se um ano entregue pelo usuario é bissexto

#Variavel que recebe do usuario o ano que sera verificado 
ano = int(input("Insira o ano: \n"))

#Variaveis necessarias para a verificação 
ano_bi1 = ano % 400
ano_bi2 = ano % 4
ano_bi3 = ano % 100

#Condição para determinar se o ano é bissexto ou não e mostrar na tela o resultado
if ano_bi1 == 0 or ano_bi2 == 0 and ano_bi3 != 0:
    print(f"\n{ano} é bissexto")
else:
    print(f"\n{ano} não é bissexto")