#   João Gabriel Nóbrega Santos
#               20242014050013
#
#   Programa para descobrir quantos palindromos existem entre 10 e 100000

#variaveis contadoras
num = 10
palindromos = 0
porcentagem = 0

#Laço que descobre quantos palindromos existem entre 10 e 100000
while num <= 100000:
    #Variaveis usadas para inverter o numero
    inverter = num
    invertido = 0
    
    #laço que inverte o numero
    while inverter > 0:
        x = inverter % 10   
        inverter //= 10 
        invertido = (invertido * 10) + x 
    
    #condicional que adiciona ao numero de palindromos se o numero for um palindromo
    if invertido == num:
        palindromos += 1
    
    #condicional para verificar progresso do programa
    if num % 1000 == 0:
        porcentagem += 1
        print(porcentagem, "% concluido")
    
    num += 1

#função para mostrar o resultado
print("Existem", palindromos, "palindromos entre 10 e 100000")