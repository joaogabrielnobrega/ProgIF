#   João Gabriel Nóbrega Santos
#               20242014050013
#
#   Programa para descobrir os pares de primos seguidos

#variavel de contagem
num = 2

#variavel de progresso
porcentagem = 0

#variavel que terá o resultado do problema
pares_primos = ""

#laço que descobre os pares impares primos seguidos 
while num <= 100000:
    #variaveis e condicional que verifica se o numero é primo
    div = 2
    ndiv = 0
    primo = False
    if num % 2 != 0:
        while div < (num / 2):
            if num % div == 0:
                ndiv += 1
            div += 1
        if ndiv == 0:
            primo = True
        
    #variaveis, condicionais para verificar se o impar seguinte do numero primo é primo
    div = 2
    ndiv = 0
    if primo:
        verifica_primo = num + 2
    
    if primo and verifica_primo % 2 != 0:
        while div < (verifica_primo / 2):
            if verifica_primo % div == 0:
                ndiv += 1
            div += 1
        if ndiv == 0:
            par_primo = True
            #variavel que adiciona um par impar seguido à variavel resposta
            pares_primos += f"({num}, {verifica_primo})"
    
    #condicional para verificar progresso do programa
    if num % 1000 == 0:
        porcentagem += 1
        print(porcentagem, "% concluido")
    num += 1

#função que mostra o resultado
print("Esse são os pares de impares primos seguidos: ", pares_primos)